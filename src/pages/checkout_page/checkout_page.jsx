import styles from "./checkout_page.module.css";
import logo from "../../images/logo.png";
import arrowGray from "../../images/gray_right_arrow.svg";
import arrowWhite from "../../images/arrow_white.svg";
import inActiveApplyIcon from "../../images/inactive_apply_icon.svg";
import activeApplyIcon from "../../images/active_apply_icon.svg";
import blackArrow from "../../images/black_arrow.svg";
import "swiper/css";
import "swiper/css/navigation";
import "swiper/css/grid";

import { useNavigate } from "react-router";
import { useEffect, useState } from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import { FreeMode, Navigation, Grid } from "swiper/modules";
import CheckoutProductCard from "../../components/checkout_product_card/checkout_product_card";
import useWindowDimensions from "../../components/hooks/windowDimensions";
import { useStores } from "../../store/store_context";
import { observer } from "mobx-react-lite";

const CheckoutPage = observer(() => {
  const navigate = useNavigate();
  const [visible, setVisible] = useState([
    [false],
    [1, 0, 0],
    [0, 0, 0, 0],
    [1, 0],
    [false, false],
  ]);
  const [loading, setLoading] = useState(false);
  const copyVisible = Array.from(visible);
  const { width } = useWindowDimensions();
  const { pageStore } = useStores();
  const [groupedCart, setGroupedCart] = useState([{}]);

  const date = new Date();
  let days = ["Вс", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб"];

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
  useEffect(() => {
    setGroupedCart(
      Object.entries(groupById(Array.from(pageStore.cart))).map(
        ([id, items]) => {
          console.log(`ID: ${id}`);
          console.log(items.length);
          console.log(pageStore.cart);
          return {
            Name: items[0].name,
            Price: items[0].price * 100,
            Quantity: items.length,
            Amount: items[0].price * items.length * 100,
            PaymentMethod: "full_payment",
            PaymentObject: "service",
            Tax: "none",
          };
        }
      )
    );
    console.log(
      Object.entries(groupById(Array.from(pageStore.cart))).map(
        ([id, items]) => {
          console.log(`ID: ${id}`);
          console.log(items.length);
          console.log(pageStore.cart);
          return {
            Name: items[0].name,
            Price: items[0].price,
            Quantity: items.length,
            Amount: items[0].price * items.length,
            PaymentMethod: "full_payment",
            PaymentObject: "service",
            Tax: "none",
          };
        }
      )
    );
  }, [pageStore.cart]);

  // Функция для оформления заказа
  const handleCheckout = async () => {
    setLoading(true);
    console.log(groupedCart);
    console.log(groupedCart[0], groupedCart[0].Amount);
    console.log(
      groupedCart.reduce((acc, elem) => {
        console.log(acc, elem.Amount, acc + elem.Amount);
        return acc + elem.Amount;
      }, 0)
    );
    const orderData = {
      amount: groupedCart.reduce((acc, elem) => acc + elem.Amount, 0),
      order_id: String(Math.random() * 1000 + Math.random() * 100),
      description: `Заказ ${groupedCart.reduce(
        (acc, elem) => acc + `${elem.Name} ${elem.Quantity} ${elem.Amount} `,
        ""
      )} Улица: ${document.querySelector("input[name='street']").value},
        Квартира: ${document.querySelector("input[name='flat']").value},
        Этаж: ${document.querySelector("input[name='floor']").value},
        Подьезд: ${document.querySelector("input[name='entrance']").value},
        Домофон: ${document.querySelector("input[name='intercom']").value},
        Комментарий к заказу: ${
          document.querySelector("input[name='comment']").value
        },`,
      phone: document.querySelector("input[name='phone']").value,
      email: document.querySelector("input[name='email']").value,
      items: groupedCart,
    };

    try {
      const response = await fetch("https://stvol.garden:8888/init-payment", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(orderData),
      });

      if (response.ok) {
        const result = await response.json();
        alert("Заказ успешно оформлен!");
        console.log(result); // Вывод ответа сервера
        window.location.href = result.payment_url;
      } else {
        alert("Ошибка при оформлении заказа!");
      }
    } catch (error) {
      console.error("Ошибка:", error);
      alert("Не удалось оформить заказ!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={width >= 500 ? styles.container : styles.container375}>
      <div className={styles.header}>
        <img src={logo} alt="" />
        <div className={styles.backButton} onClick={() => navigate(-1)}>
          <img src={arrowGray} alt="" />
        </div>
      </div>

      <p className={styles.namePageText}>Оформление заказа</p>
      <main>
        <div className={styles.userInfo}>
          <p className={styles.nameText}>{pageStore?.name}</p>
          <p className={styles.contactsText}>{pageStore?.phone}</p>
        </div>
        <p className={styles.adressText}>Адрес доставки</p>
        <div className={styles.adressData}>
          <input type="text" name="street" placeholder="Улица" required />
          <div className={styles.adressRow}>
            <input type="number" name="flat" placeholder="Квартира" required />
            <input type="number" name="floor" placeholder="Этаж" required />
          </div>
          <div className={styles.adressRow}>
            <input
              type="number"
              name="entrance"
              placeholder="Подъезд"
              required
            />
            <input type="text" name="intercom" placeholder="Домофон" required />
          </div>
          <input
            type="text"
            name="comment"
            placeholder="Комментарий для курьера"
          />
          <input type="text" name="email" placeholder="Почта" />
          <input type="text" name="phone" placeholder="Телефон" />
        </div>

        <div className={styles.checkoutOrderButton} onClick={handleCheckout}>
          {loading ? <p>Оформляем заказ...</p> : <p>Оформить заказ</p>}
        </div>
      </main>
    </div>
  );
});

export default CheckoutPage;
