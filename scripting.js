const leaf1 = document.querySelector(".leaf1");

let lastScrollY = window.scrollY;

window.addEventListener("scroll", () => {
    if (lastScrollY < window.scrollY) {
        leaf1.classList.add("leaf1--hidden");
    } else {
        leaf1.classList.remove("leaf1--hidden");
    }
    lastScrollY = window.scrollY;
});
