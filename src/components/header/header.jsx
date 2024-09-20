import styles from "./header.module.css";

import logo from "../../images/logo.svg";
import cartIcon from "../../images/cart_icon.svg";
import { useNavigate } from "react-router";
import useWindowDimensions from "../hooks/windowDimensions";

const Header = () => {
  const navigate = useNavigate();
  const { width } = useWindowDimensions();
  return (
    <div className={width >= 500 ? styles.container : styles.container375}>
      <img src={logo} alt="" className={styles.logoImg} />
      <div className={styles.cartButton} onClick={() => navigate("/cart")}>
        <img src={cartIcon} alt="" />
      </div>
    </div>
  );
};

export default Header;
