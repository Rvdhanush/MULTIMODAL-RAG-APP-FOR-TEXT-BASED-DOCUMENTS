document.getElementById('queryForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    optimizePrompt();
});

async function optimizePrompt() {
    var promptInput = document.getElementById('promptInput').value;
    var responseCard = document.getElementById('responseCard');
    var loader = document.getElementById('loader');

    // Display loader while fetching data
    loader.style.display = 'block';
    responseCard.style.display = 'none';
    try {
        const formData = new FormData();
        formData.append('question', promptInput);

        let resp = await fetch('/get_answer', {
            method: 'POST',
            body: formData
        });
        
        let data = await resp.json();
        responseCard.innerHTML = `
            <div class="row">
                <div class="col-sm-8">
                    <h6><b>Question:</b> ${promptInput}</h6>
                    <h6><b>Answer:</b></h6>
                    ${data.result} <!-- This will render the list of points -->
                </div>
                <div class="col-sm-4">
                    <img src="data:image/jpeg;base64, ${data.relevant_images || ''}" alt="" width="100%" height="auto">
                </div>
            </div>
        `;
    } catch (error) {
        responseCard.innerHTML = `<p>Error: ${error.message}</p>`;
    }
    loader.style.display = 'none';
    responseCard.style.display = 'block';
}
