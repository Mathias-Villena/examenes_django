const API_URL = 'http://localhost:8000/api';

// Función para cambiar entre secciones
function showSection(sectionId) {
    document.querySelectorAll('.section-container').forEach(section => {
        section.classList.remove('active');
    });
    document.getElementById(sectionId).classList.add('active');
}

// Event listeners para navegación
document.getElementById('view-quotes').addEventListener('click', (e) => {
    e.preventDefault();
    showSection('quotes-section');
});

document.getElementById('add-new').addEventListener('click', (e) => {
    e.preventDefault();
    showSection('forms-section');
});

// Función para cargar las citas
async function loadQuotes() {
    try {
        const response = await fetch(`${API_URL}/quotes/`);
        const quotes = await response.json();
        const container = document.getElementById('quotes-container');
        const quoteSelect = document.getElementById('quote-select');
        
        // Actualizar el contenedor de citas
        if (quotes.length === 0) {
            container.innerHTML = `
                <div class="text-center py-5">
                    <i class="fas fa-quote-right fa-3x text-muted mb-3"></i>
                    <p class="lead">No hay citas guardadas aún. ¡Sé el primero en compartir una!</p>
                </div>
            `;
        } else {
            container.innerHTML = quotes.map(quote => `
                <div class="card quote-card mb-4" data-aos="fade-up">
                    <div class="card-body">
                        <p class="quote-text">"${quote.text}"</p>
                        <p class="quote-author">- ${quote.author}</p>
                        <div class="songs-container">
                            ${quote.songs && quote.songs.length > 0 ? quote.songs.map(song => `
                                <div class="song-player">
                                    <div class="song-info">
                                        <i class="fas fa-music me-2"></i>
                                        <span>${song.title} - ${song.artist}</span>
                                    </div>
                                    <div class="custom-audio-player">
                                        <audio 
                                            src="${song.audio_clip}"
                                            data-song-id="${song.id}"
                                            preload="metadata">
                                            Tu navegador no soporta el elemento de audio.
                                        </audio>
                                        <div class="audio-controls">
                                            <button class="play-btn" onclick="togglePlay(this)">
                                                <i class="fas fa-play"></i>
                                            </button>
                                            <div class="progress-bar">
                                                <div class="progress"></div>
                                            </div>
                                            <span class="time">0:00</span>
                                        </div>
                                    </div>
                                </div>
                            `).join('') : '<p class="text-muted mt-2">No hay canciones asociadas a esta cita.</p>'}
                        </div>
                    </div>
                </div>
            `).join('');

            // Inicializar los reproductores de audio
            initializeAudioPlayers();
        }

        // Actualizar el select de citas
        quoteSelect.innerHTML = `
            <option value="">Selecciona una cita...</option>
            ${quotes.map(quote => `
                <option value="${quote.id}">${quote.text.substring(0, 50)}...</option>
            `).join('')}
        `;
    } catch (error) {
        console.error('Error al cargar las citas:', error);
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'No se pudieron cargar las citas'
        });
    }
}

// Función para inicializar los reproductores de audio
function initializeAudioPlayers() {
    document.querySelectorAll('.custom-audio-player audio').forEach(audio => {
        const player = audio.closest('.custom-audio-player');
        const progressBar = player.querySelector('.progress');
        const timeDisplay = player.querySelector('.time');
        
        // Actualizar la barra de progreso
        audio.addEventListener('timeupdate', () => {
            const progress = (audio.currentTime / audio.duration) * 100;
            progressBar.style.width = progress + '%';
            timeDisplay.textContent = formatTime(audio.currentTime);
        });

        // Manejar clicks en la barra de progreso
        player.querySelector('.progress-bar').addEventListener('click', (e) => {
            const bounds = e.currentTarget.getBoundingClientRect();
            const percent = (e.clientX - bounds.left) / bounds.width;
            audio.currentTime = percent * audio.duration;
        });

        // Cuando termina la canción
        audio.addEventListener('ended', () => {
            const playBtn = player.querySelector('.play-btn');
            playBtn.innerHTML = '<i class="fas fa-play"></i>';
            progressBar.style.width = '0%';
            timeDisplay.textContent = '0:00';
        });
    });
}

// Función para formatear el tiempo
function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    seconds = Math.floor(seconds % 60);
    return `${minutes}:${seconds.toString().padStart(2, '0')}`;
}

// Función para reproducir/pausar
function togglePlay(button) {
    const player = button.closest('.custom-audio-player');
    const audio = player.querySelector('audio');
    
    // Pausar todos los otros audios
    document.querySelectorAll('.custom-audio-player audio').forEach(otherAudio => {
        if (otherAudio !== audio && !otherAudio.paused) {
            otherAudio.pause();
            const otherBtn = otherAudio.closest('.custom-audio-player').querySelector('.play-btn');
            otherBtn.innerHTML = '<i class="fas fa-play"></i>';
        }
    });

    if (audio.paused) {
        audio.play();
        button.innerHTML = '<i class="fas fa-pause"></i>';
    } else {
        audio.pause();
        button.innerHTML = '<i class="fas fa-play"></i>';
    }
}

// Manejar el envío del formulario de citas
document.getElementById('quote-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const quoteData = {
        text: document.getElementById('quote-text').value,
        author: document.getElementById('quote-author').value
    };

    try {
        const response = await fetch(`${API_URL}/quotes/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(quoteData)
        });

        if (response.ok) {
            document.getElementById('quote-form').reset();
            loadQuotes();
            Swal.fire({
                icon: 'success',
                title: '¡Éxito!',
                text: 'Cita guardada correctamente',
                showConfirmButton: false,
                timer: 1500
            });
            showSection('quotes-section');
        } else {
            throw new Error('Error al guardar la cita');
        }
    } catch (error) {
        console.error('Error:', error);
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'No se pudo guardar la cita'
        });
    }
});

// Manejar el envío del formulario de canciones
document.getElementById('song-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('title', document.getElementById('song-title').value);
    formData.append('artist', document.getElementById('song-artist').value);
    formData.append('quote', document.getElementById('quote-select').value);
    formData.append('audio_clip', document.getElementById('song-file').files[0]);

    try {
        const response = await fetch(`${API_URL}/songs/`, {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            document.getElementById('song-form').reset();
            loadQuotes();
            Swal.fire({
                icon: 'success',
                title: '¡Éxito!',
                text: 'Canción guardada correctamente',
                showConfirmButton: false,
                timer: 1500
            });
            showSection('quotes-section');
        } else {
            throw new Error('Error al guardar la canción');
        }
    } catch (error) {
        console.error('Error:', error);
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'No se pudo guardar la canción'
        });
    }
});

// Cargar las citas cuando se carga la página
document.addEventListener('DOMContentLoaded', () => {
    loadQuotes();
    showSection('quotes-section');
});