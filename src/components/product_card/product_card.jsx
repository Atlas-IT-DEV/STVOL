import styles from "./product_card.module.css";

import bouqet from "../../images/buket1.png";
import { Swiper, SwiperSlide } from "swiper/react";
// Import Swiper styles
import "swiper/css";
import "swiper/css/pagination";

// import "swiper/css/navigation";
import { FreeMode, Pagination } from "swiper/modules";

const ProductCard = () => {
  return (
    <div className={styles.container}>
      <Swiper
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
      <p className={styles.addButtonText}>В корзину</p>
    </div>
  );
};

export default ProductCard;
