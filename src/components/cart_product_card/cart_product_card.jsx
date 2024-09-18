import styles from "./cart_product_card.module.css";

import bouqet from "../../images/buket1.png";
import { Swiper, SwiperSlide } from "swiper/react";
// Import Swiper styles
import "swiper/css";
import "swiper/css/pagination";

// import "swiper/css/navigation";
import { FreeMode, Pagination } from "swiper/modules";
import { useNavigate } from "react-router";
import useWindowDimensions from "../hooks/windowDimensions";

const CartProductCard = () => {
  const { width } = useWindowDimensions();
  const navigate = useNavigate();
  return (
    <div className={width >= 500 ? styles.container : styles.container375}>
      <Swiper
        onClick={() => navigate("/product")}
        style={{
          "--swiper-pagination-color": "rgba(237, 237, 237, 1)",
          "--swiper-pagination-bullet-inactive-color": "rgba(131, 131, 131, 1)",
          "--swiper-pagination-bullet-inactive-opacity": "1",
          "--swiper-pagination-bullet-size": "8px",
          "--swiper-pagination-bullet-horizontal-gap": "3px",
        }}
        className={styles.slideTrack}
        modules={[FreeMode, Pagination]}
        spaceBetween={50}
        freeMode={false}
        pagination={true}
      >
        <SwiperSlide className={styles.slider}>
          <img src={bouqet} alt="" />
        </SwiperSlide>
        <SwiperSlide className={styles.slider}>
          <img src={bouqet} alt="" />
        </SwiperSlide>
        <SwiperSlide className={styles.slider}>
          <img src={bouqet} alt="" />
        </SwiperSlide>
      </Swiper>
      <p className={styles.nameProductText}>Букет из роз, фиалок и ромашек</p>
      <div className={styles.priceView}>
        <p className={styles.priceText}>3050 ₽</p>
        <p className={styles.oldPriceText}>3050₽</p>
        <p className={styles.discountText}>-15%</p>
      </div>
      <p className={styles.addButtonText}>Удалить</p>
    </div>
  );
};

export default CartProductCard;
