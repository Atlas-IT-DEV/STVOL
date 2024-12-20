import Header from "../../components/header/header";
import styles from "./catalog_page.module.css";
import filterIcon from "../../images/filter_icon.svg";
import { useState, useEffect } from "react";
import BottomMenu from "../../components/bottom_menu/bottomMenu";
import ProductCard from "../../components/product_card/product_card";
import SortModal from "../../components/sort_modal/sort_modal";
import useWindowDimensions from "../../components/hooks/windowDimensions";
import { getAllBouquetsFull } from "../../components/fetches";
import { useStores } from "../../store/store_context";
import { useLocation } from "react-router";
import { observer } from "mobx-react-lite";

const CatalogPage = observer(() => {
  const { pageStore } = useStores();
  const [isPressed, setIsPressed] = useState([
    [true],
    [false, false, false, false, false, false],
  ]);
  const [ascending, setAscending] = useState(0);
  let copyIsPressed = Array.from(isPressed);
  const { width } = useWindowDimensions();
  const [bouquets, setBouquets] = useState([]);
  useEffect(() => {
    let copy_bouquets = Array.from(bouquets);
    if (ascending == 1) {
      copy_bouquets = copy_bouquets.sort((a, b) => a.price - b.price);
    } else if (ascending == 2) {
      copy_bouquets = copy_bouquets.sort((a, b) => b.price - a.price);
    }
    setBouquets(copy_bouquets);
  }, [ascending, bouquets]);

  useEffect(() => {
    setBouquets(pageStore.bouquets);
  }, [pageStore.bouquets]);

  const location = useLocation();

  useEffect(() => {
    // Сохранение позиции при уходе со страницы
    const saveScrollPosition = () => {
      sessionStorage.setItem(
        "catalogScrollPosition",
        window.scrollY.toString()
      );
    };

    window.addEventListener("beforeunload", saveScrollPosition);

    return () => {
      saveScrollPosition();
      window.removeEventListener("beforeunload", saveScrollPosition);
    };
  }, []);

  useEffect(() => {
    // Восстановление позиции при возвращении
    const savedPosition = sessionStorage.getItem("catalogScrollPosition");
    if (savedPosition) {
      window.scrollTo(0, parseInt(savedPosition, 10));
    }
  }, [location]);

  return (
    <div className={width >= 500 ? styles.container : styles.container375}>
      <div className={styles.header}>
        <Header />
      </div>
      <p className={styles.namePageText}>Каталог</p>

      <div className={styles.SortFilterButtons}>
        <SortModal ascending={ascending} setAscending={setAscending} />
        {/*         <div
          className={styles.filterButton}
          onClick={() => {
            copyIsPressed[0][0] = !copyIsPressed[0][0];
            setIsPressed(copyIsPressed);
          }}
        >
          <img src={filterIcon} alt="" />
        </div> */}
      </div>

      {/* <div
        className={isPressed[0][0] ? styles.filtersOpen : styles.filtersClose}
      >
        <p
          className={`${styles.filterButtons} ${
            isPressed[1][0]
              ? styles.activeFilterButton
              : styles.inActiveFilterButton
          }`}
          onClick={() => {
            copyIsPressed[1][0] = !copyIsPressed[1][0];
            setIsPressed(copyIsPressed);
          }}
        >
          Розы
        </p>
        <p
          className={`${styles.filterButtons} ${
            isPressed[1][1]
              ? styles.activeFilterButton
              : styles.inActiveFilterButton
          }`}
          onClick={() => {
            copyIsPressed[1][1] = !copyIsPressed[1][1];
            setIsPressed(copyIsPressed);
          }}
        >
          Тюльпаны
        </p>
        <p
          className={`${styles.filterButtons} ${
            isPressed[1][2]
              ? styles.activeFilterButton
              : styles.inActiveFilterButton
          }`}
          onClick={() => {
            copyIsPressed[1][2] = !copyIsPressed[1][2];
            setIsPressed(copyIsPressed);
          }}
        >
          Пионы
        </p>
        <p
          className={`${styles.filterButtons} ${
            isPressed[1][3]
              ? styles.activeFilterButton
              : styles.inActiveFilterButton
          }`}
          onClick={() => {
            copyIsPressed[1][3] = !copyIsPressed[1][3];
            setIsPressed(copyIsPressed);
          }}
        >
          Орхидеи
        </p>
        <p
          className={`${styles.filterButtons} ${
            isPressed[1][4]
              ? styles.activeFilterButton
              : styles.inActiveFilterButton
          }`}
          onClick={() => {
            copyIsPressed[1][4] = !copyIsPressed[1][4];
            setIsPressed(copyIsPressed);
          }}
        >
          Пионы
        </p>
        <p
          className={`${styles.filterButtons} ${
            isPressed[1][5]
              ? styles.activeFilterButton
              : styles.inActiveFilterButton
          }`}
          onClick={() => {
            copyIsPressed[1][5] = !copyIsPressed[1][5];
            setIsPressed(copyIsPressed);
          }}
        >
          Герберы
        </p>
      </div> */}
      <p className={styles.nameFilterText}>Летние букеты</p>
      <div className={styles.products}>
        <div className={styles.productsView}>
          {bouquets?.map((elem) => (
            <ProductCard
              name={elem.name}
              price={elem.price}
              uri={elem.urls[0]}
              id={elem.id}
              oldPrice={elem.old_price}
              discount={elem.discount}
              flowers={elem.flowers}
              object={elem}
            />
          ))}
        </div>
      </div>
      <BottomMenu />
    </div>
  );
});

export default CatalogPage;
