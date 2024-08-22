import BottomMenu from "../../components/bottomMenu";
import styles from "./info_page.module.css";
import logo from "../../images/logo.png";
import {
  arrowDown,
  arrowUp,
  emailIcon,
  notificationIcon,
  telegramIcon,
  telezhkaIcon,
  whatsAppIcon,
} from "../../images/images";
import { useState } from "react";

const InfoPage = () => {
  const [isOpen, setIsOpen] = useState([false, false, false]);
  const copyIsOpen = Array.from(isOpen);

  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <img src={logo} alt="" width={141} />
        <div className={styles.headerButtons}>
          <div>{notificationIcon}</div>
          <div>{telezhkaIcon}</div>
        </div>
      </header>
      <main className={styles.mainContent}>
        <p className={`${styles.mainInfo} ${styles.attributes}`}>
          — сервис доставки цветов по <br />
          Москве, России и миру
        </p>
        <p className={styles.mainText}>
          Мы — служба доставки цветов <br />и подарков по России и миру.
        </p>
        <p className={styles.mainText}>
          У нас вы легко найдёте поздравление
          <br /> для любого случая и сможете отправить <br />
          его близким, где бы они не находились.
        </p>
        <div>
          <div
            className={`${styles.attributes} ${styles.deliveryInfo}`}
            onClick={() => {
              copyIsOpen[0] === false
                ? (copyIsOpen[0] = true)
                : (copyIsOpen[0] = false);
              setIsOpen((isOpen) => (isOpen = copyIsOpen));
            }}
          >
            <p>Доставка</p>
            {isOpen[0] ? arrowUp : arrowDown}
          </div>
          {isOpen[0] ? (
            <div>
              <p className={`${styles.deliveryText} ${styles.timeDelivery}`}>
                с 9:00 до 00:00
              </p>
              <div className={styles.timePrice}>
                <div className={styles.timePriceField}>
                  <p className={styles.deliveryText}>от 3х часов</p>
                  <p className={styles.deliveryText}>FREE</p>
                </div>
                <div className={styles.timePriceField}>
                  <p className={styles.deliveryText}>за 1 час</p>
                  <p className={styles.deliveryText}>500 ₽</p>
                </div>
                <div className={styles.timePriceField}>
                  <p className={styles.deliveryText}>к точному времени</p>
                  <p className={styles.deliveryText}>300 ₽</p>
                </div>
              </div>

              <p className={styles.helpDeliveryText}>
                (дольше 15 минут курьер не ждет)
              </p>
              <div className={styles.additionalDelivery}>
                <p className={styles.helpDeliveryText}>
                  + корректировка времени при пробках
                </p>
                <p className={styles.helpDeliveryText}>
                  + повторная доставка — 500₽ (базовый тариф)
                </p>
              </div>
            </div>
          ) : null}
          <div
            className={`${styles.attributes} ${styles.refundInfo}`}
            onClick={() => {
              copyIsOpen[1] === false
                ? (copyIsOpen[1] = true)
                : (copyIsOpen[1] = false);
              setIsOpen((isOpen) => (isOpen = copyIsOpen));
            }}
          >
            <p>Возврат</p>
            {isOpen[1] ? arrowUp : arrowDown}
          </div>
          {isOpen[1] ? <div>?????</div> : null}
          <div
            className={`${styles.attributes} ${styles.loyaltyInfo}`}
            onClick={() => {
              copyIsOpen[2] === false
                ? (copyIsOpen[2] = true)
                : (copyIsOpen[2] = false);
              setIsOpen((isOpen) => (isOpen = copyIsOpen));
            }}
          >
            <p>Программа лояльности</p>
            {isOpen[2] ? arrowUp : arrowDown}
          </div>
          {isOpen[2] ? (
            <div className={styles.loyalityInfo}>
              <div className={styles.loyalityField}>
                <div>
                  <p className={styles.loyaltyText}>Бронзовый STVOL</p>
                  <p className={styles.helpLoyaltyText}>15 000 ₽ - 50 000 ₽</p>
                </div>
                <p className={styles.loyaltyText}>5%</p>
              </div>

              <div className={styles.loyalityField}>
                <div>
                  <p className={styles.loyaltyText}>Серебряный STVOL</p>
                  <p className={styles.helpLoyaltyText}>15 000 ₽ - 50 000 ₽</p>
                </div>
                <p className={styles.loyaltyText}>7%</p>
              </div>

              <div className={styles.loyalityField}>
                <div>
                  <p className={styles.loyaltyText}>Золотой STVOL</p>
                  <p className={styles.helpLoyaltyText}>15 000 ₽ - 50 000 ₽</p>
                </div>
                <p className={styles.loyaltyText}>10%</p>
              </div>
            </div>
          ) : null}
        </div>
      </main>
      <footer className={styles.aboutCompany}>
        <div className={styles.requisites}>
          <div>
            <p
              className={`${styles.aboutCompanyAttributes} ${styles.aboutCompanyText}`}
            >
              ИП
            </p>
            <p
              className={`${styles.aboutCompanyValues} ${styles.aboutCompanyText}`}
            >
              ИП STVOL букет
            </p>
          </div>
          <div>
            <p
              className={`${styles.aboutCompanyAttributes} ${styles.aboutCompanyText}`}
            >
              ОКВЭД
            </p>
            <p
              className={`${styles.aboutCompanyValues} ${styles.aboutCompanyText}`}
            >
              ИП STVOL букет
            </p>
          </div>
          <div>
            <p
              className={`${styles.aboutCompanyAttributes} ${styles.aboutCompanyText}`}
            >
              ИНН
            </p>
            <p
              className={`${styles.aboutCompanyValues} ${styles.aboutCompanyText}`}
            >
              34567865436
            </p>
          </div>
        </div>
        <div className={styles.contacts}>
          <div className={styles.telegramButton}>
            {telegramIcon}
            <p className={styles.telegramButtonText}>@STVOL</p>
          </div>

          <div className={styles.numberField}>
            {whatsAppIcon}
            <p className={styles.numberText}>+7 927 927 43 53</p>
          </div>

          <div className={styles.emailField}>
            {emailIcon}
            <p className={styles.emailText}>bhewfj@jfj.ru</p>
          </div>
        </div>
      </footer>
      <BottomMenu />
    </div>
  );
};

export default InfoPage;
