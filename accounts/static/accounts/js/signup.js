const prevButton = document.querySelector('.prev');
const nextButton = document.querySelectorAll('.next'); 
const carousel = document.querySelector('.carousel');



let index = 0; 
console.log(prevButton);
// prevButton.addEventListener('click', () => { 
//     let imageWidth = document.querySelector('.big-box').offsetWidth;
//     if (index === 0) return;
//     index-=1;
//     carousel.style.transform = `translate3d(-${ imageWidth* index}px, 0, 0)`;
// }); 

for (let a = 1 ;a<4;a++) {
    console.log(nextButton[a-1]);
    nextButton[a-1].addEventListener('click', () => { 
    let imageWidth = document.querySelector('.big-box').offsetWidth;
    console.log(imageWidth);
    if (index === 4) return;
    index+=1;
    carousel.style.transform = `translate3d(-${imageWidth * index}px, 0, 0)`;
    })

};

// function getLocation() {
//     if (navigator.geolocation) {
//         // GPS를 지원하면
//         navigator.geolocation.getCurrentPosition(
//             function (position) {
//                 const latitude = position.coords.latitude;
//                 const longitude = position.coords.longitude;
//                 const coords = position.coords;
//                 console.log(latitude);
//                 var geocoder = new kakao.maps.services.Geocoder();
//                 function searchAddrFromCoords(coords, callback) {
//                     // 좌표로 행정동 주소 정보를 요청합니다
//                     geocoder.coord2RegionCode(coords.longitude, coords.latitude, callback);
//                 }
//                 searchAddrFromCoords(coords, displayCenterInfo);

//                 function displayCenterInfo(result, status) {
//                     if (status === kakao.maps.services.Status.OK) {
//                         for (var i = 0; i < result.length; i++) {
//                             // 행정동의 region_type 값은 'H' 이므로
//                             if (result[i].region_type === "H") {
//                                 const address = result[0].region_2depth_name;
//                                 console.log( address);
//                                 const input = document.querySelector(`.location`);
//                                 input.value = address;
//                                 break;
//                             }
//                         }
//                     }
//                 }
//             },
//             function (error) {
//                 console.error(error);
//             },
//             {
//                 enableHighAccuracy: false,
//                 maximumAge: 0,
//                 timeout: Infinity,
//             }
//         );
//     } else {
//         alert("GPS를 지원하지 않습니다");
//     }
// }
// const onLocation = () => {
//     getLocation();
// };
