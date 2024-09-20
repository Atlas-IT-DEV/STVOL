import styles from "./header.module.css";

import logo from "../../images/logo.svg";
import cartIcon from "../../images/cart_icon.svg";
import { useNavigate } from "react-router";

const Header = () => {
  const navigate = useNavigate();
  return (
    <div className={styles.container}>
      <img src={logo} alt="" />
      <div className={styles.cartButton} onClick={() => navigate("/cart")}>
        <img src={cartIcon} alt="" />
      </div>
    </div>
  );
};

export default Header;
