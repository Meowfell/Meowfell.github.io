function searchNotes() {
    // Get the search input
    const input = document.getElementById('search-input').value.toLowerCase();
    const notes = document.querySelectorAll('.text-content p');

    // Loop through all paragraphs in the text-content div
    notes.forEach(note => {
        // Check if the note contains the search keyword
        if (note.innerText.toLowerCase().includes(input)) {
            // If found, highlight the note
            note.style.backgroundColor = 'yellow';
        } else {
            // If not found, remove any highlight
            note.style.backgroundColor = '';
        }
    });
}
