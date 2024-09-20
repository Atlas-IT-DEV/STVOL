import { useState } from "react";
import constructorIcon from "../../images/constructor_icon.svg";
import profileIcon from "../../images/profile_icon.svg";
import catalogIcon from "../../images/catalog_icon.svg";
import logo from "../../images/logo.svg";
import { useNavigate } from "react-router";
import styles from "./bottomMenu.module.css";
import useWindowDimensions from "../hooks/windowDimensions";

const BottomMenu = () => {
  const [isActive, setIsActive] = useState([0, 0, 1, 0]);
  const navigate = useNavigate();
  const { width } = useWindowDimensions();
  return (
    <div className={width >= 500 ? styles.container : styles.container375}>
      <div className={styles.button} onClick={() => navigate("/profile")}>
        <img src={profileIcon} alt="" className={styles.profileIcon} />
        <p>Профиль</p>
      </div>
      <div className={styles.button} onClick={() => navigate("/catalog")}>
        <img src={catalogIcon} alt="" className={styles.catalogIcon} />
        <p>Каталог</p>
      </div>
      <div className={styles.button} onClick={() => navigate("/")}>
        <img src={constructorIcon} width={43} />
        <p>Конструктор</p>
      </div>
      <div className={styles.button} onClick={() => navigate("/about")}>
        <img src={logo} width={97} />
        <p>О нас</p>
      </div>
    </div>
  );
};

export default BottomMenu;
