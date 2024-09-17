import { useState } from "react";
import constructorIcon from "../../images/constructor_icon.png";
import profileIcon from "../../images/profile_icon.svg";
import catalogIcon from "../../images/catalog_icon.svg";
import logo from "../../images/logo.png";
import { useNavigate } from "react-router";
import styles from "./bottomMenu.module.css";

const BottomMenu = () => {
  const [isActive, setIsActive] = useState([0, 0, 1, 0]);
  const navigate = useNavigate();
  return (
    <div className={styles.container}>
      <div className={styles.button} onClick={() => navigate("/profile")}>
        <img src={profileIcon} alt="" />
        <p>Профиль</p>
      </div>
      <div className={styles.button} onClick={() => navigate("/catalog")}>
        <img src={catalogIcon} alt="" />
        <p>Каталог</p>
      </div>
      <div className={styles.button} onClick={() => navigate("/")}>
        <img src={constructorIcon} width={43} />
        <p>Конструктор</p>
      </div>
      <div className={styles.button} onClick={() => navigate("/info")}>
        <img src={logo} width={97} />
        <p>О нас</p>
      </div>
    </div>
  );
};

export default BottomMenu;
