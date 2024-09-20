import styles from "./select_flower.module.css";
import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/css";
import "swiper/css/navigation";
import "swiper/css/grid";

// import "swiper/css/navigation";
import { FreeMode, Navigation, Grid } from "swiper/modules";
import FlowerCard from "../flower_card/flower_card";
import useWindowDimensions from "../hooks/windowDimensions";

const SelectFlower = () => {
  const { width } = useWindowDimensions();
  return (
    <div className={width >= 500 ? styles.container : styles.container375}>
      <Swiper
        style={{
          "--swiper-navigation-color": "rgba(167, 167, 167, 1)",
          "--swiper-navigation-size": "20px",
        }}
        className={styles.slideTrack}
        modules={[FreeMode, Navigation, Grid]}
        spaceBetween={36}
        freeMode={true}
        navigation={true}
        slidesPerView={3}
        grid={{ rows: 2, fill: "row" }}
      >
        <SwiperSlide className={styles.slider}>
          <FlowerCard />
        </SwiperSlide>
        <SwiperSlide className={styles.slider}>
          <FlowerCard />
        </SwiperSlide>
        <SwiperSlide className={styles.slider}>
          <FlowerCard />
        </SwiperSlide>
        <SwiperSlide className={styles.slider}>
          <FlowerCard />
        </SwiperSlide>
        <SwiperSlide className={styles.slider}>
          <FlowerCard />
        </SwiperSlide>
        <SwiperSlide className={styles.slider}>
          <FlowerCard />
        </SwiperSlide>
        <SwiperSlide className={styles.slider}>
          <FlowerCard />
        </SwiperSlide>
        <SwiperSlide className={styles.slider}>
          <FlowerCard />
        </SwiperSlide>
        <SwiperSlide className={styles.slider}>
          <FlowerCard />
        </SwiperSlide>
        <SwiperSlide className={styles.slider}>
          <FlowerCard />
        </SwiperSlide>
        <SwiperSlide className={styles.slider}>
          <FlowerCard />
        </SwiperSlide>
        <SwiperSlide className={styles.slider}>
          <FlowerCard />
        </SwiperSlide>
      </Swiper>
    </div>
  );
};

export default SelectFlower;
