document.addEventListener("DOMContentLoaded", function () {
    // Все элементы с классом 'rating'
    const ratings = document.querySelectorAll('.rating');

    // Пройти по каждому элементу 'rating'
    ratings.forEach(ratingElement => {
        // Получить рейтинг из атрибута data-rating
        const ratingValue = parseFloat(ratingElement.getAttribute('data-rating'));

        // Найти все звезды в текущем рейтинге
        const stars = ratingElement.querySelectorAll('.fa-star');

        // Рассчитать количество полных звезд
        const fullStars = Math.floor(ratingValue / 2);
        const halfStar = (ratingValue % 2) >= 0.5;

        // Добавить или удалить класс "is-fade" для звезд
        stars.forEach((star, index) => {
            if (index < fullStars) {
                star.classList.remove('is-fade'); // Полные звезды
            } else if (index === fullStars && halfStar) {
                star.classList.add('fa-star-half-o'); // Половина звезды
                star.classList.remove('is-fade');
            } else {
                star.classList.add('is-fade'); // Пустые звезды
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const loadMoreBtn = document.getElementById('loadMoreBtn');

    loadMoreBtn.addEventListener('click', function () {
        // Найти все скрытые элементы отзывов
        const hiddenReviews = document.querySelectorAll('.review-item-container[style*="display: none"]');

        // Показать все скрытые отзывы
        hiddenReviews.forEach(review => {
            review.style.display = 'block';
        });

        // После отображения всех отзывов скрываем кнопку
        loadMoreBtn.style.display = 'none';
    });
});