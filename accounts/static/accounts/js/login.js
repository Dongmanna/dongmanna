const prevButton = document.querySelector('.prev');
const nextButton = document.querySelector('.next'); 
const carousel = document.querySelector('.carousel');



let index = 0; 

prevButton.addEventListener('click', () => { 
    let imageWidth = document.querySelector('.description').offsetWidth;
    if (index === 0) return;
    index-=1;
    console.log(imageWidth);
    carousel.style.transform = `translate3d(-${ imageWidth* index}px, 0, 0)`;
}); 

nextButton.addEventListener('click', () => { 
    let imageWidth = document.querySelector('.description').offsetWidth;
    if (index === 7) return;
    index+=1;
    carousel.style.transform = `translate3d(-${imageWidth * index}px, 0, 0)`;


});

