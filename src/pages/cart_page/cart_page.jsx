import styles from "./cart_page.module.css";
import logo from "../../images/logo.png";
import arrowGray from "../../images/gray_right_arrow.svg";
import { useNavigate } from "react-router";
import CartProductCard from "../../components/cart_product_card/cart_product_card";
import useWindowDimensions from "../../components/hooks/windowDimensions";

const CartPage = () => {
  const navigate = useNavigate();
  const { width } = useWindowDimensions();
  return (
    <div className={width >= 500 ? styles.container : styles.container375}>
      <div className={styles.header}>
        <img src={logo} alt="" />
        <div className={styles.backButton} onClick={() => navigate(-1)}>
          <img src={arrowGray} alt="" />
        </div>
      </div>
      <p className={styles.namePageText}>Корзина</p>
      <div style={{ display: "flex", justifyContent: "center" }}>
        <div className={styles.productsView}>
          <CartProductCard />
          <CartProductCard />
          <CartProductCard />
          <CartProductCard />
          <CartProductCard />
        </div>
      </div>
      <div
        className={styles.checkoutButton}
        onClick={() => navigate("/checkout")}
      >
        <p>К оформлению</p>
      </div>
    </div>
  );
};

export default CartPage;
