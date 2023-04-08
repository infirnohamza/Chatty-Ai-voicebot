let isRecording = false;
let mediaRecorder;
let audioChunks = [];
let sessionId;

fetch('/new_session')
  .then(response => response.json())
  .then(data => {
    sessionId = data.session_id;
  })
  .catch(error => {
    console.error('Error fetching new session:', error);
  });

async function recordAudio() {
    const recordButton = document.getElementById('recordButton');
    if (!isRecording) {
        isRecording = true;
        recordButton.innerHTML = 'Stop Recording';
        const stream = await navigator.mediaDevices.getUserMedia({audio: true});
        mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.start();

        mediaRecorder.addEventListener("dataavailable", event => {
            audioChunks.push(event.data);
        });

        mediaRecorder.addEventListener("stop", () => {
            const audioBlob = new Blob(audioChunks, {type: 'audio/mpeg'});
            audioChunks = [];
            sendAudio(audioBlob);
        });
    } else {
        isRecording = false;
        recordButton.innerHTML = 'Record and Send';
        mediaRecorder.stop();
    }
}

function sendAudio(audioBlob) {
    const loadingElement = document.getElementById('loading');
    loadingElement.style.display = 'block'; // Show the loading element

    const formData = new FormData();
    formData.append('audio', audioBlob);
    fetch(`/chat/${sessionId}`, {
        method: 'POST',
        body: formData
    }).then(response => {
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return response.json();
    }).then(responseData => {
        loadingElement.style.display = 'none'; // Hide the loading element

        const conversation = document.getElementById('conversation');

        const userMessage = document.createElement('div');
        userMessage.classList.add('message', 'user');
        userMessage.innerText = responseData.user_text;
        conversation.appendChild(userMessage);

        const assistantMessage = document.createElement('div');
        assistantMessage.classList.add('message', 'assistant');
        assistantMessage.innerText = responseData.assistant_text;
        conversation.appendChild(assistantMessage);

        // Fetch the audio file
        fetch(responseData.assistant_audio).then(audioResponse => {
            if (!audioResponse.ok) {
                throw new Error("Audio response was not ok");
            }
            return audioResponse.blob();
        }).then(audioBlob => {
            const audioElement = document.createElement('audio');
            audioElement.src = URL.createObjectURL(audioBlob);
            audioElement.controls = true;
            conversation.appendChild(audioElement);

            // Automatically play the AI assistant's reply
            audioElement.play();
        }).catch(error => {
            console.error('Error fetching audio:', error);
        });

    }).catch(error => {
        loadingElement.style.display = 'none'; // Hide the loading element in case of error
        console.error('Error:', error);
    });
}

function deleteChatSession() {
    fetch(`/delete_session/${sessionId}`, {
      method: 'DELETE',
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.status === 'success') {
          console.log('Chat session deleted');
        } else {
          console.error('Error deleting chat session:', data.message);
        }
      })
      .catch((error) => {
        console.error('Error deleting chat session:', error);
      });
}
