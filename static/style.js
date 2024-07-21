const eyeIcon = document.getElementById("eye-icon");
const loginPassword = document.getElementById("password");








let profile = document.querySelector('.nav-action-btn');
let menu = document.querySelector('.user-menu');

profile.onclick = function () {
    menu.classList.toggle('active');
}






var swipercategory = new Swiper(".category_container", {
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    breakpoints: {

      400: {
        slidesPerView: 3,
        spaceBetween: 10,
      },
        600: {
          slidesPerView: 3,
          spaceBetween: 10,
        },
        768: {
          slidesPerView: 4,
          spaceBetween: 40,
        },
        1400: {
          slidesPerView: 6,
          spaceBetween: 15,
        },
      },
  });


const panelBtns = document.querySelectorAll("[data-panel-btn]");
const sidePanels = document.querySelectorAll("[data-side-panel]");

for (let i = 0; i < panelBtns.length; i++) {
  panelBtns[i].addEventListener("click", function () {

    let clickedElemDataValue = this.dataset.panelBtn;

    for (let i = 0; i < sidePanels.length; i++) {

      if (clickedElemDataValue === sidePanels[i].dataset.sidePanel) {
        sidePanels[i].classList.toggle("actives");
      } else {
        sidePanels[i].classList.remove("actives");
      }

    }

  });
}




const imgs = document.querySelectorAll('.img-select a');
const imgBtns = [...imgs];
let imgId = 1;

imgBtns.forEach((imgItem) => {
    imgItem.addEventListener('click', (event) => {
        event.preventDefault();
        imgId = imgItem.dataset.id;
        slideImage();
    });
});

function slideImage(){
    const displayWidth = document.querySelector('.img-showcase img:first-child').clientWidth;

    document.querySelector('.img-showcase').style.transform = `translateX(${- (imgId - 1) * displayWidth}px)`;
}

window.addEventListener('resize', slideImage);


'use strict';



/**
 * navbar toggle
 */

const overlay = document.querySelector("[data-overlay]");
const navOpenBtn = document.querySelector("[data-nav-open-btn]");
const navbar = document.querySelector("[data-navbar]");
const navCloseBtn = document.querySelector("[data-nav-close-btn]");

const navElems = [overlay, navOpenBtn, navCloseBtn];

for (let i = 0; i < navElems.length; i++) {
  navElems[i].addEventListener("click", function () {
    navbar.classList.toggle("active");
    overlay.classList.toggle("active");
  });
}



/**
 * header & go top btn active on page scroll
 */

const header = document.querySelector("[data-header]");
const goTopBtn = document.querySelector("[data-go-top]");

window.addEventListener("scroll", function () {
  if (window.scrollY >= 80) {
    header.classList.add("active");
    goTopBtn.classList.add("active");
  } else {
    header.classList.remove("active");
    goTopBtn.classList.remove("active");
  }
});



const searchContainer = document.querySelector("[data-search-wrapper]");
const searchBtn = document.querySelector("[data-search-btn]");

searchBtn.addEventListener("click", function () {
  searchContainer.classList.toggle("active");
});


// Password Show Hide icon toggle
eyeIcon.onclick = () => {
  if (loginPassword.type == "password") {
      loginPassword.type = "text";
      eyeIcon.classList.add("fa-eye")
      eyeIcon.classList.remove("fa-eye-slash")
      eyeIcon.style.color = "green"
  }
  else {
      loginPassword.type = "password"
      eyeIcon.classList.remove("fa-eye")
      eyeIcon.classList.add("fa-eye-slash")
      eyeIcon.style.color = "red"
  }
}


const allStar = document.querySelectorAll('.rating .star')
const ratingValue = document.querySelector('.rating input')

allStar.forEach((item, idx)=> {
	item.addEventListener('click', function () {
		let click = 0
		ratingValue.value = idx + 1

		allStar.forEach(i=> {
			i.classList.replace('bxs-star', 'bx-star')
			i.classList.remove('active')
		})
		for(let i=0; i<allStar.length; i++) {
			if(i <= idx) {
				allStar[i].classList.replace('bx-star', 'bxs-star')
				allStar[i].classList.add('active')
			} else {
				allStar[i].style.setProperty('--i', click)
				click++
			}
		}
	})
})





		function togglePopup() { 
			const overlay = document.getElementById('popupOverlay'); 
			overlay.classList.toggle('show'); 
		} 



// user profile image uploadf
function handleImage(e) {
  e.preventDefault();
  const uploadedImage = e.target.files[0];
  if (!uploadedImage) return;

  const fileReader = new FileReader();
  fileReader.readAsDataURL(uploadedImage);

  fileReader.onload = function () {
      const avatarPreviewImage = document.querySelector(".avatar-preview-image");
      const avatarDefaultIcon = document.querySelector(".avatar-default-icon");

      avatarPreviewImage.src = this.result;
      avatarPreviewImage.classList.remove("hidden");
      avatarPreviewImage.style.display = "block";
      avatarDefaultIcon.classList.add("hidden");
      avatarDefaultIcon.style.display = "none";

      userInput.avatar = this.result;
  };
}





