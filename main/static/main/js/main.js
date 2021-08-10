
window.addEventListener('scroll',scrollEvent);
// document.querySelector(".search-box").style.transform="translate(0,10px)";
// document.querySelector(".search-box").style.opacity="1";

function scrollEvent(){
    let scrHeight = document.documentElement.scrollTop;
    console.log(scrHeight);
    if(20<scrHeight && scrHeight<1200){
        document.querySelector("body").style.backgroundColor="#9dc39c";
    } else if( 1200 <=scrHeight && scrHeight<2150){
        document.querySelector("body").style.backgroundColor="#fbfaf6";
    } else {
        document.querySelector("body").style.backgroundColor="#9dc39c";
    }
    
        
        // 박스2 애니메이션 
    if (scrHeight>=1100 && scrHeight <2200){
        document.querySelector(".my-group").style.transform="translate(0,0)";
        document.querySelector(".my-group").style.opacity="1";
    } else{
        document.querySelector(".my-group").style.transform="translate(-100px,0)";
        document.querySelector(".my-group").style.opacity="0";
    }
}
