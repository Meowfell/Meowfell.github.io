function searchNotes() {
    // Get the search input value
    var searchText = document.getElementById("search-input").value.trim().toLowerCase();
    
    // Get all paragraphs to search within
    var paragraphs = document.querySelectorAll(".text-content p");

    // Loop through each paragraph
    paragraphs.forEach(function(paragraph) {
        // Get the text content of the paragraph
        var paragraphText = paragraph.textContent.toLowerCase();

        // Check if the search text is found within the paragraph
        if (paragraphText.includes(searchText)) {
            // Split the paragraph text by the search text to insert <mark> tags
            var parts = paragraphText.split(new RegExp('(' + searchText + ')', 'gi'));
            paragraph.innerHTML = ''; // Clear existing content

            // Reconstruct the paragraph with <mark> tags around the search text
            parts.forEach(function(part) {
                var mark = document.createElement('mark');
                if (part.toLowerCase() === searchText) {
                    mark.textContent = part;
                } else {
                    mark.textContent = part;
                }
                paragraph.appendChild(mark);
            });
        }
    });
}
