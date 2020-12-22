const slidePage = document.querySelector(".slide-page");
const nextBtnFirst = document.querySelector(".firstNext");
const prevBtnSec = document.querySelector(".prev-1");
const nextBtnSec = document.querySelector(".next-1");
const prevBtnThird = document.querySelector(".prev-2");
const nextBtnThird = document.querySelector(".next-2");
const prevBtnFourth = document.querySelector(".prev-3");
const submitBtn = document.querySelector(".submit");
const progressText = document.querySelectorAll(".step p");
const progressCheck = document.querySelectorAll(".step .check");
const bullet = document.querySelectorAll(".step .bullet");
let current = 1;

nextBtnFirst.addEventListener("click", function (event) {
  event.preventDefault();
  slidePage.style.marginLeft = "-25%";
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current - 1].classList.add("active");
  current += 1;
});
nextBtnSec.addEventListener("click", function (event) {
  event.preventDefault();
  slidePage.style.marginLeft = "-50%";
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current - 1].classList.add("active");
  current += 1;
});
nextBtnThird.addEventListener("click", function (event) {
  event.preventDefault();
  slidePage.style.marginLeft = "-75%";
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current - 1].classList.add("active");
  current += 1;
});
submitBtn.addEventListener("click", function () {
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current - 1].classList.add("active");
  current += 1;
  setTimeout(function () {
    alert("Your Form Successfully Signed up");
    location.reload();
  }, 800);
});

prevBtnSec.addEventListener("click", function (event) {
  event.preventDefault();
  slidePage.style.marginLeft = "0%";
  bullet[current - 2].classList.remove("active");
  progressCheck[current - 2].classList.remove("active");
  progressText[current - 2].classList.remove("active");
  current -= 1;
});
prevBtnThird.addEventListener("click", function (event) {
  event.preventDefault();
  slidePage.style.marginLeft = "-25%";
  bullet[current - 2].classList.remove("active");
  progressCheck[current - 2].classList.remove("active");
  progressText[current - 2].classList.remove("active");
  current -= 1;
});
prevBtnFourth.addEventListener("click", function (event) {
  event.preventDefault();
  slidePage.style.marginLeft = "-50%";
  bullet[current - 2].classList.remove("active");
  progressCheck[current - 2].classList.remove("active");
  progressText[current - 2].classList.remove("active");
  current -= 1;
});

//form subdivisions
let division = document.getElementById('division');
let edu = document.getElementById('edu');
let dept = document.getElementById('department');

division.onclick = function () {
  if (division.value == 'state' || division.value == 'outreach') {
    document.getElementById('state').classList.remove('hidden');

    document.getElementById('society').classList.add('hidden');
    document.getElementById('initiative').classList.add('hidden');
  }
  else if (division.value == 'society') {
    document.getElementById('society').classList.remove('hidden');

    document.getElementById('state').classList.add('hidden');
    document.getElementById('initiative').classList.add('hidden');
  }
  else if (division.value == 'initiative') {
    document.getElementById('initiative').classList.remove('hidden');

    document.getElementById('society').classList.add('hidden');
    document.getElementById('state').classList.add('hidden');
  }
  else if (division.value == 'national') {
    document.getElementById('initiative').classList.add('hidden');
    document.getElementById('society').classList.add('hidden');
    document.getElementById('state').classList.add('hidden');
  }
}

edu.onclick = function () {
  if (edu.value == 'school' || edu.value == 'college') {
    document.getElementById('edu-level').classList.remove('hidden');
  }
  else {
    document.getElementById('edu-level').classList.add('hidden');
  }
}

dept.onclick = function () {
  if (dept.value == 'marketing') {
    document.getElementById('marketing').classList.remove('hidden');
    document.getElementById('it').classList.add('hidden');
    document.getElementById('pub-rel').classList.add('hidden');
    document.getElementById('finance').classList.add('hidden');
  }
  else if (dept.value == 'it') {
    document.getElementById('marketing').classList.add('hidden');
    document.getElementById('it').classList.remove('hidden');
    document.getElementById('pub-rel').classList.add('hidden');
    document.getElementById('finance').classList.add('hidden');
  }
  else if (dept.value == 'pub-rel') {
    document.getElementById('marketing').classList.add('hidden');
    document.getElementById('it').classList.add('hidden');
    document.getElementById('pub-rel').classList.remove('hidden');
    document.getElementById('finance').classList.add('hidden');
  }
  else if (dept.value == 'finance') {
    document.getElementById('marketing').classList.add('hidden');
    document.getElementById('it').classList.add('hidden');
    document.getElementById('pub-rel').classList.add('hidden');
    document.getElementById('finance').classList.remove('hidden');
  }
  else {
    document.getElementById('marketing').classList.add('hidden');
    document.getElementById('it').classList.add('hidden');
    document.getElementById('pub-rel').classList.add('hidden');
    document.getElementById('finance').classList.add('hidden');
  }
}

//submit
function disableSubmit() {
  document.getElementById("submit").disabled = true;
  document.getElementById("submit").style.cursor = "not-allowed";
}

function activateButton(element) {

  if (element.checked) {
    document.getElementById("submit").style.cursor = "pointer";
    document.getElementById("submit").disabled = false;
  }
  else {
    document.getElementById("submit").style.cursor = "not-allowed";
    document.getElementById("submit").disabled = true;
  }
}