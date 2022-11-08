// TO-DO 
// Add in event listener that allows images to fade off the screen as the user scrolls further down 

// leaves
const leaf1 = document.querySelector(".leaf1");
const leaf2 = document.querySelector(".leaf2");

// vines
const vine1 = document.querySelector(".vine1");
const vine2 = document.querySelector(".vine1-1");




let lastScrollY = window.scrollY;

window.addEventListener("scroll", () => {
    if (lastScrollY < window.scrollY && lastScrollY < 30) {
        leaf1.style.transform = "translateY(-" + lastScrollY + "px)";
        // leaves
            leaf1.style.transform = `translateX(${window.scrollY * 0.5}px)`;
            leaf2.style.transform = `translateX(${window.scrollY * 0.3}px)`;
        // vines
            vine1.style.transform = `translateX(${window.scrollY * 0.5 * -1}px)`;
            vine2.style.transform = `translateX(${window.scrollY * 0.75 * -1}px)`;
    } else {
        // leaves
            leaf1.style.transform = `translateX(${window.scrollY * 0.5}px)`;
            leaf2.style.transform = `translateX(${window.scrollY * 0.3}px)`;

        // vines
            vine1.style.transform = `translateX(${window.scrollY * 0.5 * -1}px)`;
            vine2.style.transform = `translateX(${window.scrollY * 0.75 * -1}px)`;

    }
    lastScrollY = window.scrollY;
});
