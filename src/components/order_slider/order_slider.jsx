import styles from "./order_slider.module.css";
import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/css";
import "swiper/css/navigation";
// import "swiper/css/navigation";
import { FreeMode, Navigation } from "swiper/modules";
import OrderCard from "../order_card/order_card";

const OrderSlider = () => {
  return (
    <div className={styles.container}>
      <Swiper
        style={{
          "--swiper-navigation-color": "rgba(167, 167, 167, 1)",
          "--swiper-navigation-size": "14px",
        }}
        className={styles.slideTrack}
        modules={[FreeMode, Navigation]}
        spaceBetween={36}
        freeMode={false}
        navigation={true}
        slidesPerView={1}
      >
        <SwiperSlide className={styles.slider}>
          <OrderCard />
        </SwiperSlide>
        <SwiperSlide className={styles.slider}>
          <OrderCard />
        </SwiperSlide>
      </Swiper>
    </div>
  );
};

export default OrderSlider;
