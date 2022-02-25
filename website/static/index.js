/* sending request to the backend */
function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/"; /* refresh page redirect and reload endpoint */
    });
}