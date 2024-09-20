import styles from "./cart_page.module.css";
import logo from "../../images/logo.png";
import arrowGray from "../../images/gray_right_arrow.svg";
import { useNavigate } from "react-router";
import CartProductCard from "../../components/cart_product_card/cart_product_card";
import useWindowDimensions from "../../components/hooks/windowDimensions";
import { useStores } from "../../store/store_context";
import { observer } from "mobx-react-lite";
import ProductCard from "../../components/product_card/product_card";
import { useEffect } from "react";
import { useState } from "react";

const CartPage = observer(() => {
  const navigate = useNavigate();
  const { width } = useWindowDimensions();
  const { pageStore } = useStores();
  const [products, setProducts] = useState(null);
  const groupById = (arr) => {
    const grouped = {};

    arr.forEach((elem) => {
      if (!grouped[elem.id]) {
        grouped[elem.id] = []; // Если такой id еще не встречался, создаем массив
      }
      grouped[elem.id].push(elem); // Добавляем элемент в массив для данного id
    });

    return grouped;
  };

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
          {Object.entries(groupById(Array.from(pageStore.cart))).map(
            ([id, items]) => {
              console.log(`ID: ${id}`);
              console.log(items.length);
              console.log(pageStore.cart);
              return (
                <ProductCard
                  name={items[0].name}
                  price={items[0].price}
                  uri={items[0].url}
                  id={items[0].id}
                  oldPrice={items[0].old_price}
                  discount={items[0].discount}
                  flowers={items[0].flowers}
                  object={items[0]}
                  isCart={true}
                  num={items.length}
                />
              );
            }
          )}
          {/* {pageStore.cart.map((elem) => (
            <ProductCard
              name={elem.name}
              price={elem.price}
              uri={elem.url}
              id={elem.id}
              oldPrice={elem.old_price}
              discount={elem.discount}
              flowers={elem.flowers}
              object={elem}
              isCart={true}
            />
          ))} */}
        </div>
      </div>
      <button
        className={styles.checkoutButton}
        disabled={pageStore.cart.length > 0 ? false : true}
        onClick={() => navigate("/checkout")}
      >
        <p>К оформлению</p>
      </button>
    </div>
  );
});

export default CartPage;
