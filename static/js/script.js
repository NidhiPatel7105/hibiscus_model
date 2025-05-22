document.addEventListener("DOMContentLoaded", function() {
    const fileInput = document.getElementById("fileInput");
    const uploadBtn = document.getElementById("uploadBtn");
    const captureBtn = document.getElementById("captureBtn");
    const resultContainer = document.getElementById("resultContainer");

    // Upload Image & Predict
    uploadBtn.addEventListener("click", function() {
        if (fileInput.files.length === 0) {
            alert("Please select an image to upload.");
            return;
        }

        const formData = new FormData();
        formData.append("file", fileInput.files[0]);

        fetch("/upload", { method: "POST", body: formData })
        .then(response => response.json())
        .then(data => {
            resultContainer.innerHTML = `<h2>Predicted: ${data.prediction}</h2>
                                         <img src="${data.image_url}" width="250">`;
        });
    });

    // Capture Image & Predict
    captureBtn.addEventListener("click", function() {
        fetch("/capture")
        .then(response => response.json())
        .then(data => {
            resultContainer.innerHTML = `<h2>Predicted: ${data.prediction}</h2>
                                         <img src="${data.image_url}" width="250">`;
        });
    });
});
