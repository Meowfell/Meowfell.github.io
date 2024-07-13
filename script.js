function searchNotes() {
    const input = document.getElementById('search-input').value.trim().toLowerCase();
    const notes = document.querySelectorAll('.text-content p');

    // Loop through all paragraphs in the text-content div
    notes.forEach(note => {
        const noteText = note.innerText.toLowerCase();
        
        // Check if the note contains the search keyword
        if (noteText.includes(input)) {
            // Highlight the note
            note.style.backgroundColor = 'yellow';
            
            // Scroll to the note
            note.scrollIntoView({ behavior: 'smooth', block: 'center' });
        } else {
            // Remove any previous highlight
            note.style.backgroundColor = '';
        }
    });

    // If no results found, alert the user
    if (!input) {
        alert('Please enter a search term.');
    } else {
        let found = false;
        notes.forEach(note => {
            if (note.innerText.toLowerCase().includes(input)) {
                found = true;
            }
        });
        if (!found) {
            alert('No results found.');
        }
    }
}
