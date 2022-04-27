let links = document.querySelectorAll(".header .container .links li");
let style =document.querySelector("head style")
let header_height =document.querySelector(".header").clientHeight
console.log(header_height)
for (let link of links){
    link.onmouseover = function(){
        link.classList.add("active");
        style.innerHTML = `.header .container .links .active:before{transition:.4s ease; width:100%}
        .header .container .links >.active> a{
            color:var(--main-color);
        }
        `;
    };
    link.onmouseleave =function(){
        style.innerHTML = `.header .container .links li:before{transition:.4s ease; width:0%}`
        link.classList.remove("active")
    }
}





