const IMG_URL = 'https://image.tmdb.org/t/p/w185_and_h278_bestv2';



//menu
const leftMenu = document.querySelector('.left-menu');
const hamburger = document.querySelector('.hamburger');
const tvShowsList = document.querySelector('.tv-shows__list');
const modal = document.querySelector('.modal');
const tvShows = document.querySelector('.tv-shows');
const tvCardIMG = document.querySelector('.tv-card__img');
const modalTitle = document.querySelector('.modal__title');
const genrestList = document.querySelector('.genres-list');
const rating = document.querySelector('.rating');
const description = document.querySelector('.description');
const modalLink = document.querySelector('.modal__link');
const searchForm = document.querySelector('.search__form');
const searchFormInput = document.querySelector('.search__form-input');
const preloader = document.querySelector('.preloader');
const tvSearchHead = document.querySelector('.tv-shows__head');
const dropdownLink = document.querySelectorAll('.dropdown');

//const loading = document.createElement('div');
//loading.className = 'loading';



const DBService = class {

    constructor(){
        this.API_KEY = '480196c2327c49ff2ccd60121777b3d6';
        this.SERVER = 'https://api.themoviedb.org/3';
    }

    getData = async (url) => {
        const res = await fetch(url);
        if(res.ok){
            return res.json();
        }
        else{
            throw new Error(`Не удалось получить данные по адресу ${url}`);
        }
    }

    getTestData = () => {
        return this.getData('test.json');
    }

    getTestCard = () => {
        return this.getData('card.json');
    }

    getSearchResult = (query) => {
        return this.getData(`${this.SERVER}/search/tv?api_key=${this.API_KEY}&query=${query}&language=ru-RU`);
    }

    getTvShow = (id) => {
        return this.getData(this.SERVER + '/tv/' + id + '?api_key='+this.API_KEY+'&language=ru-RU');
    }

    getTopRated = () => this.getData(this.SERVER + '/tv/top_rated?api_key=' + this.API_KEY + '&language=ru-RU');

    getPopular = () => this.getData(this.SERVER + '/tv/popular?api_key=' + this.API_KEY + '&language=ru-RU');

    getToday = () => this.getData(this.SERVER + '/tv/airing_today?api_key=' + this.API_KEY + '&language=ru-RU');

    getWeek = () => this.getData(this.SERVER + '/tv/on_the_air?api_key=' + this.API_KEY + '&language=ru-RU');
    
}

const renderCard = (response, target) => {

    tvShowsList.textContent = ''

    if(response.results.length != 0){

        tvSearchHead.textContent = target ? target.textContent : '';

        response.results.forEach((item) => {
            console.log(item);
            const {
                backdrop_path:backdrop,
                name:title,
                poster_path:poster,
                vote_average:vote,
                id
                 } = item;
    
    
            const posterIMG = poster ? IMG_URL + poster : 'img/no-poster.jpg';
            const backdropIMG = backdrop && poster ? IMG_URL + backdrop :  'img/no-poster.jpg';
            const voteElem = vote != 0 ? vote : ``;
            const voteHide = vote == 0 ? 'hide' : '';
            
            const card = document.createElement('li');
            card.className ='tv-shows__item';
            card.innerHTML = `
            <a href="#" id="${id}" class="tv-card">
                <span class="tv-card__vote ${voteHide}">${voteElem}</span>
                <img class="tv-card__img"
                    src="${posterIMG}"
                    data-backdrop="${backdropIMG}"
                    alt=${title}>
                <h4 class="tv-card__head">${title}</h4>
            </a>
            `;
    
            //loading.remove();
            preloader.classList.add('hide');
            tvShowsList.append(card);
        });
    }else{
        tvSearchHead.textContent = 'По вашему запросу ничего не найдено';
        preloader.classList.add('hide');
    }

    
}

searchForm.addEventListener('submit', (event)=>{
    event.preventDefault();
    const value = searchFormInput.value.trim();
    if(value){
        //tvShows.append(loading);
        preloader.classList.remove('hide');
        new DBService().getSearchResult(value).then(renderCard);
    }
    searchFormInput.value = '';
})



//open/close menu

const closeDropdown = () => {
    dropdownLink.forEach(item =>{
        item.classList.remove('active');
    });
}

hamburger.addEventListener('click', () => {
    leftMenu.classList.toggle('openMenu');
    hamburger.classList.toggle('open');
    closeDropdown();
});

document.addEventListener('click', (event) => {
    if(!event.target.closest('.left-menu')){
        leftMenu.classList.remove('openMenu');
    hamburger.classList.remove('open');
    closeDropdown();
    }
});

leftMenu.addEventListener('click', (event) => {
    event.preventDefault();
    const target = event.target;
    const dropdown = target.closest('.dropdown');
    if(dropdown){
        dropdown.classList.toggle('active');
        leftMenu.classList.add('openMenu');
        hamburger.classList.add('open');
    }

    if(target.closest('#search')){
        tvShowsList.textContent = '';
        tvSearchHead.textContent = '';
    }
    if(target.closest('#top-rated')){
        preloader.classList.remove('hide');
        new DBService().getTopRated().then((response) => renderCard(response, target));
    }
    if(target.closest('#popular')){
        preloader.classList.remove('hide');
        new DBService().getPopular().then((response) => renderCard(response, target));
    }
    if(target.closest('#today')){
        preloader.classList.remove('hide');
        new DBService().getToday().then((response) => renderCard(response, target));
    }
    if(target.closest('#week')){
        preloader.classList.remove('hide');
        new DBService().getWeek().then((response) => renderCard(response, target));
    }

    
});

//open modal window

tvShowsList.addEventListener('click', (event) => {

    event.preventDefault();

    const target = event.target;
    const card = target.closest('.tv-card');
    
    if(card){

        preloader.classList.remove('hide');

        new DBService().getTvShow(card.id)
        .then(data => {
            tvCardIMG.src = data.poster_path ? IMG_URL + data.poster_path : 'img/no-poster.jpg';
            modalTitle.textContent = data.name;
            genrestList.textContent = '';
            data.genres.forEach(item =>{
                genrestList.innerHTML += `<li>${item.name}</li>`;
            });
            rating.textContent = data.vote_average;
            description.textContent = data.overview;
            modalLink.href = data.homepage;
        }).then(()=>{
            document.body.style.overflow = 'hidden';
            modal.classList.remove('hide');
            preloader.classList.add('hide');
        });
    }
});

//close modaal window

modal.addEventListener('click', (evengt)=>{
    if(event.target.closest('.cross') || event.target.classList.contains('modal')){
        document.body.style.overflow = '';
        modal.classList.add('hide');
    }
});

//card reverse

const changeImage = event =>{
    const card = event.target.closest('.tv-shows__item');

    if(card){
        const img = card.querySelector('.tv-card__img');

        if(img.dataset.backdrop){
            [img.src, img.dataset.backdrop] = [img.dataset.backdrop, img.src];
        }
    }
};

window.addEventListener('load', () => {
    preloader.classList.remove('hide');
    new DBService().getTopRated().then((response) => renderCard(response));
});

tvShowsList.addEventListener('mouseover', changeImage);
tvShowsList.addEventListener('mouseout', changeImage);