import Header from "../../components/header/header";
import styles from "./product_page.module.css";
import arrowGray from "../../images/gray_right_arrow.svg";
import arrowWhite from "../../images/arrow_white.svg";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router";
import { useLocation } from "react-router";
import useWindowDimensions from "../../components/hooks/windowDimensions";
import { getBouquetByIdFull } from "../../components/fetches";

const ProductPage = () => {
  const [count, setCount] = useState(1);
  const [isOpen, setIsOpen] = useState([false, false, false, false]);
  const copyIsOpen = Array.from(isOpen);
  const navigate = useNavigate();
  const [bouquet, setBouquet] = useState({});
  const getBouquetInfo = async () => {
    setBouquet(await getBouquetByIdFull(location.state.product_id));
  };
  useEffect(() => {
    getBouquetInfo();
  }, []);

  const { width } = useWindowDimensions();
  const location = useLocation();
  return (
    <div className={width >= 500 ? styles.container : styles.container375}>
      <div className={styles.header}>
        <Header />
      </div>
      <div className={styles.backButton} onClick={() => navigate(-1)}>
        <img src={arrowGray} alt="" />
      </div>
      <div className={styles.imageProduct}>
        <img src={bouquet?.url} alt="" />
      </div>
      <main>
        <p className={styles.nameProductText}>{bouquet?.name}</p>
        <div className={styles.sumView}>
          <p className={styles.sumText}>{bouquet?.price * count} ₽</p>
          <div className={styles.countView}>
            <p
              onClick={() => {
                setCount(count - 1);
                count != 1 ? setCount(count - 1) : setCount(1);
              }}
            >
              -
            </p>
            <p className={styles.countText}>{count}</p>
            <p onClick={() => setCount(count + 1)}>+</p>
          </div>
        </div>
        <div className={styles.orderButtons}>
          <p className={styles.addCartText}>В корзину</p>
          <p className={styles.fastOrderText}>Быстрый заказ</p>
        </div>
        <p className={`${styles.subheaderText} ${styles.descriptionHeader}`}>
          Описание
        </p>
        <p className={styles.descriptionText}>
          Бесплатная доставка по городу: <br />
          <span>
            Осуществляется бесплатно в четырехчасовой интервал в пределах МКАО
          </span>{" "}
          <br />
          <br /> Аквапак для букетов: <br />{" "}
          <span>
            Осуществляется бесплатно в четырехчасовой интервал в пределах МКАО
          </span>{" "}
          <br /> <br /> Анонимная доставка: <br />
          <span>
            Осуществляется бесплатно в четырехчасовой интервал в пределах МКАО
          </span>
        </p>
        <div
          className={styles.hideButtons}
          onClick={() => {
            copyIsOpen[0] = !copyIsOpen[0];
            setIsOpen(copyIsOpen);
          }}
        >
          <p className={styles.subheaderText}>Детали</p>
          <img
            src={arrowWhite}
            alt=""
            className={isOpen[0] ? styles.arrowUp : styles.arrowDown}
          />
        </div>
        <div className={isOpen[0] ? styles.viewOpen : styles.viewClose}>
          <p className={styles.detailsText}>
            Цветы: <br />
            <span>Ромашки, розы и фиалки</span> <br />
            <br />
            Высота: <br /> <span>35 см</span> <br /> <br />
            Диаметр: <br /> <span>50 см</span> <br /> <br />
            Упаковка: <br />{" "}
            <span>
              Осуществляется бесплатно в четырехчасовой интервал в пределах МКАО
            </span>
          </p>
        </div>
        <div
          className={styles.hideButtons}
          onClick={() => {
            copyIsOpen[1] = !copyIsOpen[1];
            setIsOpen(copyIsOpen);
          }}
        >
          <p className={styles.subheaderText}>Сохранение свежести</p>
          <img
            src={arrowWhite}
            alt=""
            className={isOpen[1] ? styles.arrowUp : styles.arrowDown}
          />
        </div>
        <div className={isOpen[1] ? styles.viewOpen : styles.viewClose}>
          <p className={styles.saveText}>
            Живые цветы требуют деликатного отношения и лучше всего сохраняются
            в температуре от +2 до +7 градусов. Не подвергайте букеты резким
            перепадам температур, а также жаре и морозу. Ни нам ни Нашим букетам
            это не нравится. <br />
            <br />  Каждый цветок уникален и имеет свой срок жизни, некоторые
            растения сохраняют свежеть дольше чем другие. Помните, что стоимость
            букета никак не влияет на то, сколько он простоит в Вашей вазе.  
            <br />
            <br /> Мы тщательно следим за свежестью наших букетов и хотим, чтобы
            Ваш STVOL был крепче и дольше стоял. <br />
            <br />
            Перед тем как поставить цветы в воду не забудьте обрезать стебли
            используя нож или секатор. При каждой замене воды стебли необходимо
            подрезать еще раз – это обеспечит растениям лучшую сохранность.
            Желательно менять воду ежедневно, что позволить препятствовать
            образованию бактерий в вазе. Не забывайте промывать вазу используя
            антибактериальное моющее средство.
            <br />
            <br /> Свежие срезанные цветы недолговечны и требуют подходящего
            места. Оно должно быть прохладным и с достаточным количеством
            свежего воздуха. Мы точно знаем, что цветы не любят прямые солнечные
            лучи, им не стоит находиться рядом с отопительными приборами, а
            также стоять на сквозняке.
            <br />
            <br /> Следите за количеством воды в вазе, это особенно важно в
            жару, а также в помещениях с сухим воздухом. Воды в емкости должно
            хватать, чтобы треть STVOL’а была погружена в воду. Для
            продолжительной сохранности цветов необходимо убирать листья и
            увядшие части цветов, попавшие в воду.
            <br />
            <br /> Мы не рекомендуем оставлять букеты надолго без воды особенно
            при транспортировке. Цветы лучше не оставлять в машине с
            неработающим кондиционером, а также подвергать резким перепадам
            температуры.
            <br />
            <br /> Если Ваш букет завял слишком быстро убедитесь, насколько
            тщательно были соблюдены наши рекомендации.
          </p>
        </div>
        <div
          className={styles.hideButtons}
          onClick={() => {
            copyIsOpen[2] = !copyIsOpen[2];
            setIsOpen(copyIsOpen);
          }}
        >
          <p className={styles.subheaderText}>Доставка</p>
          <img
            src={arrowWhite}
            alt=""
            className={isOpen[2] ? styles.arrowUp : styles.arrowDown}
          />
        </div>
        <div className={isOpen[2] ? styles.viewOpen : styles.viewClose}>
          <table>
            <tr
              style={{
                color: "rgba(55, 55, 55, 1)",
                fontSize: 20,
                fontFamily: "TTNorms700",
              }}
            >
              <td>Интервал</td>
              <td>Москва</td>
              <td>За МКАД</td>
            </tr>

            <tr
              style={{
                color: "rgba(156, 156, 156, 1)",
                fontFamily: "TTNorms400",
                fontSize: 20,
                borderBottom: "1px solid rgba(55, 55, 55, 1)",
                height: 45,
              }}
            >
              <td>Трехчасовой</td>
              <td>Бесплатно</td>
              <td>399+40₽/км</td>
            </tr>
            <tr
              style={{
                color: "rgba(156, 156, 156, 1)",
                fontFamily: "TTNorms400",
                fontSize: 20,
                borderBottom: "1px solid rgba(55, 55, 55, 1)",
                height: 45,
              }}
            >
              <td>Часовой</td>
              <td>499 ₽</td>
              <td>699+40₽/км</td>
            </tr>
            <tr
              style={{
                color: "rgba(156, 156, 156, 1)",
                fontFamily: "TTNorms400",
                fontSize: 20,
                height: 45,
              }}
            >
              <td>Точное время</td>
              <td>999 ₽</td>
              <td>1199+40₽/км</td>
            </tr>
          </table>
        </div>
        <div
          className={styles.hideButtons}
          onClick={() => {
            copyIsOpen[3] = !copyIsOpen[3];
            setIsOpen(copyIsOpen);
          }}
        >
          <p className={styles.subheaderText}>Доставка в "Москва Сити"</p>
          <img
            src={arrowWhite}
            alt=""
            className={isOpen[3] ? styles.arrowUp : styles.arrowDown}
          />
        </div>
        <div className={isOpen[3] ? styles.viewOpen : styles.viewClose}>
          <table>
            <tr
              style={{
                color: "rgba(55, 55, 55, 1)",
                fontSize: 20,
                fontFamily: "TTNorms700",
              }}
            >
              <td>Интервал</td>
              <td></td>
              <td>Москва Сити</td>
            </tr>

            <tr
              style={{
                color: "rgba(156, 156, 156, 1)",
                fontFamily: "TTNorms400",
                fontSize: 20,
                borderBottom: "1px solid rgba(55, 55, 55, 1)",
                height: 45,
              }}
            >
              <td>Трехчасовой</td>
              <td></td>
              <td>699 ₽</td>
            </tr>
            <tr
              style={{
                color: "rgba(156, 156, 156, 1)",
                fontFamily: "TTNorms400",
                fontSize: 20,
                borderBottom: "1px solid rgba(55, 55, 55, 1)",
                height: 45,
              }}
            >
              <td>Часовой</td>
              <td></td>
              <td>999 ₽</td>
            </tr>
            <tr
              style={{
                color: "rgba(156, 156, 156, 1)",
                fontFamily: "TTNorms400",
                fontSize: 20,
                height: 45,
              }}
            >
              <td>Точное время</td>
              <td></td>
              <td>1449 ₽</td>
            </tr>
          </table>
        </div>
      </main>
    </div>
  );
};

export default ProductPage;
