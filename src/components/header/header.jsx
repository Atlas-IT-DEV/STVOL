import styles from "./header.module.css";

import logo from "../../images/logo.png";
import cartIcon from "../../images/cart_icon.svg";

const Header = () => {
  return (
    <div className={styles.container}>
      <img src={logo} alt="" />
      <div className={styles.cartButton}>
        <img src={cartIcon} alt="" />
      </div>
    </div>
  );
};

export default Header;
