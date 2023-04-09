let isRecording = false;
let mediaRecorder;
let audioChunks = [];
let sessionId;
let savedMessages = [];

fetch("/firebase_config")
  .then((response) => response.json())
  .then((config) => {
    // Initialize Firebase
    firebase.initializeApp(config);

    // Get a reference to the storage service
    const storage = firebase.storage();
  })
  .catch((error) => {
    console.error("Error fetching Firebase config:", error);
  });

fetch("/new_session")
  .then((response) => response.json())
  .then((data) => {
    sessionId = data.session_id;
  })
  .catch((error) => {
    console.error("Error fetching new session:", error);
  });

async function recordAudio() {
  const recordButton = document.getElementById("recordButton");
  if (!isRecording) {
    isRecording = true;
    recordButton.innerHTML = "Stop Recording";
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start();

    mediaRecorder.addEventListener("dataavailable", (event) => {
      audioChunks.push(event.data);
    });

    mediaRecorder.addEventListener("stop", () => {
      const audioBlob = new Blob(audioChunks, { type: "audio/mpeg" });
      audioChunks = [];
      sendAudio(audioBlob);
    });
  } else {
    isRecording = false;
    recordButton.innerHTML = "Record and Send";
    mediaRecorder.stop();
  }
}

function sendAudio(audioBlob) {
  const loadingElement = document.getElementById("loading");
  loadingElement.style.display = "block"; // Show the loading element

  const formData = new FormData();
  formData.append("audio", audioBlob);
  fetch(`/chat/${sessionId}`, {
    method: "POST",
    body: formData,
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((responseData) => {
      loadingElement.style.display = "none"; // Hide the loading element

      const conversation = document.getElementById("conversation");

      const userMessage = document.createElement("div");
      userMessage.classList.add("message", "user");
      userMessage.innerText = responseData.user_text;
      conversation.appendChild(userMessage);
      savedMessages.push({
        role: "user",
        text: responseData.user_text,
        audio: audioBlob,
      });

      const assistantMessage = document.createElement("div");
      assistantMessage.classList.add("message", "assistant");
      assistantMessage.innerText = responseData.assistant_text;
      conversation.appendChild(assistantMessage);

      // Fetch the audio file
      fetch(responseData.assistant_audio)
        .then((audioResponse) => {
          if (!audioResponse.ok) {
            throw new Error("Audio response was not ok");
          }
          return audioResponse.blob();
        })
        .then((audioBlob) => {
          const audioElement = document.createElement("audio");
          audioElement.src = URL.createObjectURL(audioBlob);
          audioElement.controls = true;
          conversation.appendChild(audioElement);

          // Automatically play the AI assistant's reply
          audioElement.play();

          savedMessages.push({
            role: "assistant",
            text: responseData.assistant_text,
            audio: audioBlob,
          });
        })
        .catch((error) => {
          console.error("Error fetching audio:", error);
        });
    })
    .catch((error) => {
      loadingElement.style.display = "none"; // Hide the loading element in case of error
      console.error("Error:", error);
    });
}
async function saveSessionToFirebase(sessionId) {
  const storageRef = firebase.storage().ref();
  const sessionRef = storageRef.child(`sessions/${sessionId}.json`);

  let savedMessagesWithAudioUrls = [];

  for (let i = 0; i < savedMessages.length; i++) {
    const message = savedMessages[i];
    const audioUrl = await saveAudioToFirebase(message.audio, sessionId, message.role, i);
    savedMessagesWithAudioUrls.push({
      role: message.role,
      text: message.text,
      audioUrl: audioUrl,
    });
  }

  const sessionData = {
    sessionId: sessionId,
    messages: savedMessagesWithAudioUrls,
  };

  sessionRef.putString(JSON.stringify(sessionData))
    .then((snapshot) => {
      console.log('Session data saved to Firebase Storage.');
      document.getElementById("downloadSessionButton").disabled = false;
    })
    .catch((error) => {
      console.error('Error saving session data to Firebase Storage:', error);
    });
}

  document.getElementById("createSessionButton").addEventListener("click", () => {
    saveSessionToFirebase(sessionId);
  });
  
  
  async function downloadSession(sessionId) {
    const storageRef = firebase.storage().ref();
    const sessionRef = storageRef.child(`sessions/${sessionId}.json`);
  
    sessionRef.getDownloadURL()
      .then(async (url) => {
        const response = await fetch(url);
        const sessionData = await response.json();
  
        for (const message of sessionData.messages) {
          const audioUrl = message.audioUrl;
          const audioResponse = await fetch(audioUrl);
          const audioBlob = await audioResponse.blob();
  
          const link = document.createElement("a");
          link.href = URL.createObjectURL(audioBlob);
          link.download = `${message.role}_${sessionData.sessionId}_${message.text.slice(0, 5)}.mp3`;
          link.click();
        }
      })
      .catch((error) => {
        console.error('Error downloading session data from Firebase Storage:', error);
      });
  }
  
  document.getElementById("downloadSessionButton").addEventListener("click", () => {
    downloadSession(sessionId);
  });

  async function saveAudioToFirebase(blob, sessionId, role, index) {
    const storageRef = firebase.storage().ref();
    const audioRef = storageRef.child(`sessions/${sessionId}/${role}_${index}.mp3`);
    
    return audioRef.put(blob).then((snapshot) => {
      console.log(`Audio file ${role}_${index}.mp3 saved to Firebase Storage.`);
      return snapshot.ref.getDownloadURL();
    });
  }
  