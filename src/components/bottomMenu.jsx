import { useState } from "react";
import { catalogIcon, profileIcon } from "../images/images";
import constructorIcon from "../images/constructor_icon.png";
import logo from "../images/logo.png";
import { useNavigate } from "react-router";
import styles from "../components/bottomMenu.module.css";

const BottomMenu = () => {
  const [isActive, setIsActive] = useState([0, 0, 1, 0]);
  const navigate = useNavigate();
  return (
    <div className={styles.container}>
      <div className={styles.button} onClick={() => navigate("/profile")}>
        {profileIcon}
        <p>Профиль</p>
      </div>
      <div className={styles.button} onClick={() => navigate("/catalog")}>
        {catalogIcon}
        <p>Каталог</p>
      </div>
      <div className={styles.button}>
        <img src={constructorIcon} width={43} />
        <p>Конструктор</p>
      </div>
      <div className={styles.button}>
        <img src={logo} width={97} />
        <p>О нас</p>
      </div>
    </div>
  );
};

export default BottomMenu;
