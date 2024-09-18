import styles from "./checkout_page.module.css";
import logo from "../../images/logo.png";
import arrowGray from "../../images/gray_right_arrow.svg";
import arrowWhite from "../../images/arrow_white.svg";
import inActiveApplyIcon from "../../images/inactive_apply_icon.svg";
import activeApplyIcon from "../../images/active_apply_icon.svg";
import blackArrow from "../../images/black_arrow.svg";
import "swiper/css";
import "swiper/css/navigation";
import "swiper/css/grid";

import { useNavigate } from "react-router";
import { useState } from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import { FreeMode, Navigation, Grid } from "swiper/modules";
import CheckoutProductCard from "../../components/checkout_product_card/checkout_product_card";
import useWindowDimensions from "../../components/hooks/windowDimensions";

const CheckoutPage = () => {
  const navigate = useNavigate();
  const [visible, setVisible] = useState([
    [false],
    [1, 0, 0],
    [0, 0, 0, 0],
    [1, 0],
    [false, false],
  ]);
  const copyVisible = Array.from(visible);
  const { width } = useWindowDimensions();

  const date = new Date();
  let days = ["Вс", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб"];

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <img src={logo} alt="" />
        <div className={styles.backButton} onClick={() => navigate(-1)}>
          <img src={arrowGray} alt="" />
        </div>
      </div>

      <p className={styles.namePageText}>Оформление заказа</p>
      <main>
        <div className={styles.userInfo}>
          <p className={styles.nameText}>Имя Фамилия</p>
          <p className={styles.contactsText}>+7 961 842 40 82</p>
          <p className={styles.contactsText}>kjncks@kmcla.ru</p>
        </div>
        <p className={styles.adressText}>Адрес доставки</p>
        <div className={styles.adressData}>
          <input type="text" name="street" id="" placeholder="Улица" required />
          <div className={styles.adressRow}>
            <input
              type="number"
              name="flat"
              id=""
              placeholder="Квартира"
              required
            />
            <input
              type="number"
              name="floor"
              id=""
              placeholder="Этаж"
              required
            />
          </div>
          <div className={styles.adressRow}>
            <input
              type="number"
              name="entrance"
              id=""
              placeholder="Подъезд"
              required
            />
            <input
              type="text"
              name="intercom"
              id=""
              placeholder="Домофон"
              required
            />
          </div>
          <input
            type="text"
            name="comment"
            id=""
            placeholder="Комментарий для курьера"
          />
        </div>
        <p className={styles.timeText}>Время доставки</p>
        <div
          className={styles.intervalButton}
          onClick={() => {
            copyVisible[0][0] = !copyVisible[0][0];
            setVisible(copyVisible);
          }}
        >
          <p>Интервал</p>
          <img
            src={arrowWhite}
            alt=""
            className={visible[0][0] ? styles.arrowUp : styles.arrowDown}
          />
        </div>
        <div className={visible[0][0] ? styles.viewOpen : styles.viewClose}>
          <div className={styles.timeInterval}>
            <p
              className={`${styles.typeHourText} ${
                visible[1][0] == 1 ? styles.activeType : styles.inActiveType
              }`}
              onClick={() => {
                copyVisible[1] = [1, 0, 0];
                setVisible(copyVisible);
              }}
            >
              Трехчасовой
            </p>
            <div
              className={
                visible[1][0] == 1
                  ? styles.selectIntervalTime
                  : styles.viewClose
              }
            >
              <input type="time" name="" id="" />
              <p>-</p>
              <input type="time" name="" id="" />
            </div>
          </div>
          <div className={styles.timeInterval}>
            <p
              className={`${styles.typeHourText} ${
                visible[1][1] == 1 ? styles.activeType : styles.inActiveType
              }`}
              onClick={() => {
                copyVisible[1] = [0, 1, 0];
                setVisible(copyVisible);
              }}
            >
              Часовой
            </p>
            <div
              className={
                visible[1][1] == 1
                  ? styles.selectIntervalTime
                  : styles.viewClose
              }
            >
              <input type="time" name="" id="" />
              <p>-</p>
              <input type="time" name="" id="" />
            </div>
          </div>
          <div className={styles.timeInterval}>
            <p
              className={`${styles.typeHourText} ${
                visible[1][2] == 1 ? styles.activeType : styles.inActiveType
              }`}
              onClick={() => {
                copyVisible[1] = [0, 0, 1];
                setVisible(copyVisible);
              }}
            >
              Точное время:
            </p>
            <div
              className={
                visible[1][2] == 1
                  ? styles.selectIntervalTime
                  : styles.viewClose
              }
            >
              <input type="time" name="" id="" />
            </div>
          </div>
        </div>
        <div className={styles.selectDate}>
          <Swiper
            style={{
              "--swiper-navigation-color": "rgba(167, 167, 167, 1)",
              "--swiper-navigation-size": "20px",
            }}
            className={styles.slideTrack}
            modules={[FreeMode, Navigation, Grid]}
            spaceBetween={36}
            freeMode={false}
            navigation={true}
            slidesPerView={width >= 500 ? 3 : 2}
          >
            <SwiperSlide
              className={styles.slider}
              onClick={() => {
                copyVisible[2] = [1, 0, 0, 0];
                setVisible(copyVisible);
              }}
            >
              <div
                className={`${styles.dateCard} ${
                  visible[2][0] == 1
                    ? styles.activeDateCard
                    : styles.inActiveDateCard
                }`}
              >
                <p id="today">{date.getDate()}</p>
                <p>Сегодня</p>
              </div>
            </SwiperSlide>
            <SwiperSlide
              className={styles.slider}
              onClick={() => {
                copyVisible[2] = [0, 1, 0, 0];
                setVisible(copyVisible);
              }}
            >
              <div
                className={`${styles.dateCard} ${
                  visible[2][1] == 1
                    ? styles.activeDateCard
                    : styles.inActiveDateCard
                }`}
              >
                <p>{date.getDate() + 1}</p>
                <p>Завтра</p>
              </div>
            </SwiperSlide>
            <SwiperSlide
              className={styles.slider}
              onClick={() => {
                copyVisible[2] = [0, 0, 1, 0];
                setVisible(copyVisible);
              }}
            >
              <div
                className={`${styles.dateCard} ${
                  visible[2][2] == 1
                    ? styles.activeDateCard
                    : styles.inActiveDateCard
                }`}
              >
                <p>{date.getDate() + 2}</p>
                <p>{days[date.getDay() + 2]}</p>
              </div>
            </SwiperSlide>
            <SwiperSlide
              className={styles.slider}
              onClick={() => {
                copyVisible[2] = [0, 0, 0, 1];
                setVisible(copyVisible);
              }}
            >
              <div
                className={`${styles.dateCard} ${
                  visible[2][3] == 1
                    ? styles.activeDateCard
                    : styles.inActiveDateCard
                }`}
              >
                <p>{date.getDate() + 3}</p>
                <p>{days[date.getDay() + 3]}</p>
              </div>
            </SwiperSlide>
          </Swiper>
        </div>
        <div>
          <p className={styles.recipientText}>Получатель</p>
          <div className={styles.recipientView}>
            <div
              className={styles.selectRecipientButton}
              onClick={() => {
                copyVisible[3] = [1, 0];
                setVisible(copyVisible);
              }}
            >
              <p>Я получу заказ</p>
              <img
                src={visible[3][0] == 1 ? activeApplyIcon : inActiveApplyIcon}
                alt=""
              />
            </div>
            <div
              className={styles.selectRecipientButton}
              onClick={() => {
                copyVisible[3] = [0, 1];
                setVisible(copyVisible);
              }}
            >
              <p>Другой получатель</p>
              <img
                src={visible[3][1] == 1 ? activeApplyIcon : inActiveApplyIcon}
                alt=""
              />
            </div>
          </div>
          <div className={styles.inputRecipient}>
            <input type="text" name="" id="" placeholder="Имя получателя" />
            <input
              type="number"
              name=""
              id=""
              placeholder="Телефон получателя"
            />
          </div>

          <div className={styles.sendButtons}>
            <div
              className={styles.sendButton}
              onClick={() => {
                copyVisible[4][0] = !copyVisible[4][0];
                setVisible(copyVisible);
              }}
            >
              <p>Отправить анонимно</p>
              <img
                src={visible[4][0] ? activeApplyIcon : inActiveApplyIcon}
                alt=""
              />
            </div>
            <div
              className={styles.sendButton}
              onClick={() => {
                copyVisible[4][1] = !copyVisible[4][1];
                setVisible(copyVisible);
              }}
            >
              <p>Отправить фото перед доставкой</p>
              <img
                src={visible[4][1] ? activeApplyIcon : inActiveApplyIcon}
                alt=""
              />
            </div>
          </div>
        </div>
        <div className={styles.productCards}>
          <CheckoutProductCard />
          <CheckoutProductCard />
        </div>
        <div className={styles.resultDelivery}>
          <p className={styles.resultDeliveryText}>Итог:</p>
          <div className={styles.deliveryView}>
            <p
              className={`${styles.attributeDeliveryText} ${styles.deliveryText}`}
            >
              Доставка
            </p>
            <p className={`${styles.valueDeliveryText} ${styles.deliveryText}`}>
              599 ₽
            </p>
          </div>
          <div className={styles.deliveryView}>
            <p className={styles.attributeDeliveryText}>Cкидка</p>
            <p className={styles.valueDeliveryText}>5%</p>
          </div>
          <div className={styles.deliveryView}>
            <p
              className={`${styles.attributeDeliveryText} ${styles.sumDeliveryText}`}
            >
              Сумму заказа
            </p>
            <p
              className={`${styles.valueDeliveryText} ${styles.sumDeliveryText}`}
            >
              10 198 ₽
            </p>
          </div>
        </div>
        <div className={styles.promocodeButton}>
          <p>Введите промокод</p>
          <img src={blackArrow} alt="" />
        </div>
        <div className={styles.checkoutOrderButton}>
          <p>Оформить заказ</p>
        </div>
      </main>
    </div>
  );
};

export default CheckoutPage;
