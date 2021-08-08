
window.addEventListener('scroll',changeColor);
function changeColor(){
    let scrHeight = document.documentElement.scrollTop;
    if(scrHeight<800){
        document.querySelector(".main-main").style.backgroundColor="seagreen";
    } else {
        document.querySelector(".main-main").style.backgroundColor="#a7a856";
    }
    if (scrHeight>=400 && scrHeight <1400){
        document.querySelector(".my-group").style.transform="translate(0,0)";
        document.querySelector(".my-group").style.opacity="1";
    } else{
        document.querySelector(".my-group").style.transform="translate(-100px,0)";
        document.querySelector(".my-group").style.opacity="0";
    }
}
