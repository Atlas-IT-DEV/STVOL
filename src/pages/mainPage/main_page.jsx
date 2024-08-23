import styles from "../mainPage/main_page.module.css";
import { useNavigate } from "react-router";
import BottomMenu from "../../components/bottomMenu";
import {
  arrowRight,
  leftArrowNavigation,
  notificationIcon,
  rightArrowNavigation,
  telezhkaIcon,
} from "../../images/images";

import logo from "../../images/logo.png";
import stvol from "../../images/buket1.png";
import Flower from "../../components/flower";
import { useState } from "react";
import Packaging from "../../components/packaging";

const MainPage = ({ flowers = stvol }) => {
  const navigate = useNavigate();
  const [isActive, setIsActive] = useState([1, 0]);
  return (
    <div className={styles.container}>
      <header className={styles.headerContent}>
        <img src={logo} alt="" width={141} />
        <div className={styles.headerButtons}>
          <div>{notificationIcon}</div>
          <div>{telezhkaIcon}</div>
        </div>
      </header>
      <main className={styles.mainContent}>
        <p className={`${styles.headersText} ${styles.namePage}`}>
          Конструктор
        </p>
        <div className={styles.stvolLayout}>
          <img src={flowers} alt="" />
        </div>
        <div className={styles.buttons}>
          <div className={styles.filterButton}>
            <p
              className={styles.button}
              onClick={() => {
                setIsActive([1, 0]);
              }}
              style={
                isActive[0] == 1
                  ? { backgroundColor: "rgba(15, 15, 15, 1)" }
                  : null
              }
            >
              Цветы
            </p>
            <p
              className={styles.button}
              onClick={() => {
                setIsActive([0, 1]);
              }}
              style={
                isActive[1] == 1
                  ? { backgroundColor: "rgba(15, 15, 15, 1)" }
                  : null
              }
            >
              Упаковка
            </p>
          </div>
          <p className={styles.basketButton}>В корзину</p>
        </div>
        <div className={styles.selectedView}>
          <div>{leftArrowNavigation}</div>
          {isActive[0] == 1 ? (
            <div className={styles.selectedFlower}>
              <div className={styles.selectedRow}>
                <Flower />
                <Flower />
                <Flower />
              </div>
              <div className={styles.selectedRow}>
                <Flower />
                <Flower />
                <Flower />
              </div>
            </div>
          ) : (
            <div className={styles.selectedFlower}>
              <div className={styles.selectedRow}>
                <Packaging />
                <Packaging />
                <Packaging />
              </div>
              <div className={styles.selectedRow}>
                <Packaging />
                <Packaging />
                <Packaging />
              </div>
            </div>
          )}

          <div>{rightArrowNavigation}</div>
        </div>
        <p className={styles.helpText}>
          Подсказка: свайпни влево для того, <br />
          чтобы перейти к настройке букета
        </p>
      </main>
      <BottomMenu />
    </div>
  );
};
export default MainPage;
