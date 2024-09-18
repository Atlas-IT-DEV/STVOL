-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Сен 18 2024 г., 00:56
-- Версия сервера: 5.7.39
-- Версия PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `Stvol`
--

-- --------------------------------------------------------

--
-- Структура таблицы `adresses`
--

CREATE TABLE IF NOT EXISTS `adresses` (
  `id` int(11) NOT NULL,
  `adress` varchar(255) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `adresses`
--

INSERT IGNORE INTO `adresses` (`id`, `adress`, `user_id`) VALUES
(1, 'Покровский бульвар, д10', 1),
(2, 'Красноармейская, д24', 2),
(3, 'Гагарина, д34', 3);

-- --------------------------------------------------------

--
-- Структура таблицы `Bouquet`
--

CREATE TABLE IF NOT EXISTS `Bouquet` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `price` int(11) NOT NULL,
  `image_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `Bouquet`
--

INSERT IGNORE INTO `Bouquet` (`id`, `name`, `price`, `image_id`) VALUES
(1, 'Розовые розы', 1000, 1),
(2, 'Тюльпаны', 5000, 2),
(3, 'Одуванчики', 600, 3);

-- --------------------------------------------------------

--
-- Структура таблицы `company_data`
--

CREATE TABLE IF NOT EXISTS `company_data` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `company_data`
--

INSERT IGNORE INTO `company_data` (`id`, `name`, `description`) VALUES
(1, 'Ландышевый парк', 'Весь парк это магазин цветов'),
(2, 'Розовый переулок', 'Переулок украшен розами, можно купить редкие цветы'),
(3, 'Большой торговый центр', 'Можно приобрести все для цветов');

-- --------------------------------------------------------

--
-- Структура таблицы `images`
--

CREATE TABLE IF NOT EXISTS `images` (
  `id` int(11) NOT NULL,
  `url` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `images`
--

INSERT IGNORE INTO `images` (`id`, `url`) VALUES
(1, 'http://localhost:8000/bouquet/example1.png'),
(2, 'http://localhost:8000/bouquet/example3.png'),
(3, 'http://localhost:8000/bouquet/example4.png');

-- --------------------------------------------------------

--
-- Структура таблицы `orders`
--

CREATE TABLE IF NOT EXISTS `orders` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `total_price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `orders`
--

INSERT IGNORE INTO `orders` (`id`, `user_id`, `date`, `total_price`) VALUES
(1, 1, '2024-08-29 23:41:51', 12000),
(2, 2, '2024-08-29 23:41:51', 15000),
(3, 3, '2024-08-29 23:41:51', 10000);

-- --------------------------------------------------------

--
-- Структура таблицы `order_bouquets`
--

CREATE TABLE IF NOT EXISTS `order_bouquets` (
  `id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `bouquet_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `order_bouquets`
--

INSERT IGNORE INTO `order_bouquets` (`id`, `order_id`, `bouquet_id`, `quantity`) VALUES
(1, 1, 1, 1),
(2, 2, 2, 1),
(3, 3, 3, 2);

-- --------------------------------------------------------

--
-- Структура таблицы `ref_codes`
--

CREATE TABLE IF NOT EXISTS `ref_codes` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `code` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `ref_codes`
--

INSERT IGNORE INTO `ref_codes` (`id`, `user_id`, `code`) VALUES
(1, 1, 'awdwadawdadsads'),
(2, 2, 'dwadawdawdawdaw'),
(3, 3, 'dawfcawvawvawfa');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `telegram_id` int(11) NOT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `count_bonus` int(11) DEFAULT '0',
  `referal` tinyint(1) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `users`
--

INSERT IGNORE INTO `users` (`id`, `name`, `telegram_id`, `phone`, `count_bonus`, `referal`) VALUES
(1, 'Иван', 123456789, '79127564256', 230, 0),
(2, 'Мария', 987654321, '79136459245', 755, 0),
(3, 'Петр', 111223344, '79321645297', 331, 0);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `adresses`
--
ALTER TABLE `adresses`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Индексы таблицы `Bouquet`
--
ALTER TABLE `Bouquet`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_image_id` (`image_id`);

--
-- Индексы таблицы `company_data`
--
ALTER TABLE `company_data`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `images`
--
ALTER TABLE `images`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Индексы таблицы `order_bouquets`
--
ALTER TABLE `order_bouquets`
  ADD PRIMARY KEY (`id`,`order_id`,`bouquet_id`),
  ADD KEY `fk_bouquet_id` (`bouquet_id`),
  ADD KEY `order_bouquets_ibfk_1` (`order_id`);

--
-- Индексы таблицы `ref_codes`
--
ALTER TABLE `ref_codes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `adresses`
--
ALTER TABLE `adresses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `Bouquet`
--
ALTER TABLE `Bouquet`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `company_data`
--
ALTER TABLE `company_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `images`
--
ALTER TABLE `images`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `order_bouquets`
--
ALTER TABLE `order_bouquets`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `ref_codes`
--
ALTER TABLE `ref_codes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `adresses`
--
ALTER TABLE `adresses`
  ADD CONSTRAINT `adresses_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Ограничения внешнего ключа таблицы `Bouquet`
--
ALTER TABLE `Bouquet`
  ADD CONSTRAINT `fk_image_id` FOREIGN KEY (`image_id`) REFERENCES `images` (`id`) ON DELETE SET NULL;

--
-- Ограничения внешнего ключа таблицы `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Ограничения внешнего ключа таблицы `order_bouquets`
--
ALTER TABLE `order_bouquets`
  ADD CONSTRAINT `order_bouquets_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `order_bouquets_ibfk_2` FOREIGN KEY (`bouquet_id`) REFERENCES `Bouquet` (`id`) ON DELETE CASCADE;

--
-- Ограничения внешнего ключа таблицы `ref_codes`
--
ALTER TABLE `ref_codes`
  ADD CONSTRAINT `ref_codes_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
