document.addEventListener('DOMContentLoaded', () => {
    const viewCountElement = document.getElementById('view-count');
    const incrementButton = document.getElementById('increment-button');

    // Fetch and display the current view count
    fetch('/view_count')
        .then(response => response.json())
        .then(data => {
            viewCountElement.textContent = data.count;
        });

    // Increment the view count on button click
    incrementButton.addEventListener('click', () => {
        fetch('/increment_view', {
            method: 'POST'
        }).then(() => {
            // Fetch the updated view count
            return fetch('/view_count');
        }).then(response => response.json())
          .then(data => {
              viewCountElement.textContent = data.count;
          });
    });
});
