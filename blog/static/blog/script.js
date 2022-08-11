// ########################### Controls Back to Top button ########################################

var backTopBtn = document.getElementById("backTopBtn");
// Reacts when scrolling down
window.onscroll = function() {scrollDown();};

// Scroll up to top
function backToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

// Make the back to top button appear
function scrollDown() {
    if ( document.body.scrollTop > 30 || document.documentElement.scrollTop > 30) {
        backTopBtn.style.display = "block";
    } else {
        backTopBtn.style.display = "none";
    };
}

// ############################ Controls the slug's input ########################################
const input = document.querySelector("input[name=title]");
const slug = document.querySelector("input[name=slug]");


// Converts the title into a slug with valid url's sintax
const convertSlug = (title) => {
    return title.toString().toLowerCase().trim()
    .replace(/&/g, '_and_') // Replace & for -and-
    .replace(/[\s\W\-]+/g, "-") // Replace ' ', special characters, and '--' for a single '-'.
};

input.addEventListener("keyup", () => {
    // Gets the value of the input variable and sends it as argument to the function convertSlug()
    slug.setAttribute("value", convertSlug(input.value));
});