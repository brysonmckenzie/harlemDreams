

var span =  document.getElementsByClassName("ex")[0];

// var modal =  document.querySelector(".vid-modal")

// span.onclick = function() {
//     modal.style.display = "none";
// }


console.log('working')

function clearModal() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target === span) {
        clearModal();
    }
}

