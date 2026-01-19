import React from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import { EffectCards, Pagination } from 'swiper/modules';

import 'swiper/css';
import 'swiper/css/effect-cards';
import 'swiper/css/pagination';

export default function ContributionSlider() {
  const cardStyle = {
    borderRadius: '20px',
    padding: '2rem',
    height: '320px',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    boxSizing: 'border-box',
    background: 'linear-gradient(145deg, #0f172a 0%, #1e293b 100%)',
    border: '1px solid rgba(56, 189, 248, 0.15)',
    boxShadow: '0 30px 50px -15px rgba(0,0,0,0.5)',
    cursor: 'grab'
  };

  return (
    <div
      style={{
        maxWidth: '340px',
        margin: '0 auto',
        perspective: '1200px',
        minHeight: '380px' // 🔑 evita colapso visual
      }}
    >
      <style>{`
        .swiper {
          width: 100%;
          padding-top: 20px;
          padding-bottom: 40px;
          overflow: visible !important;
        }
        .swiper-slide {
          border-radius: 20px;
        }
        .swiper-slide-shadow {
          background: rgba(0,0,0,0.25) !important;
          border-radius: 20px;
        }
        .swiper-pagination-bullet {
          background: #64748b;
          opacity: 0.4;
        }
        .swiper-pagination-bullet-active {
          background: #38bdf8;
          opacity: 1;
          transform: scale(1.3);
        }
      `}</style>

      <Swiper
        effect="cards"
        grabCursor
        modules={[EffectCards, Pagination]}
        pagination={{ clickable: true }}
        cardsEffect={{
          perSlideOffset: 16,
          perSlideRotate: 2,
          slideShadows: true
        }}
      >
        <SwiperSlide>
          <div style={{ ...cardStyle, border: '1px solid #38bdf8' }}>
            <h3 style={{ color: '#38bdf8' }}>1. Understand Context</h3>
            <p style={{ color: '#cbd5e1' }}>
              I listen first. I ensure I understand the context, team dynamics, and operational standards before acting.
            </p>
          </div>
        </SwiperSlide>

        <SwiperSlide>
          <div style={cardStyle}>
            <h3 style={{ color: '#f8fafc' }}>2. Execute Reliably</h3>
            <p style={{ color: '#94a3b8' }}>
              I carry out tasks with precision and consistency, reducing errors and workload for the team.
            </p>
          </div>
        </SwiperSlide>

        <SwiperSlide>
          <div style={cardStyle}>
            <h3 style={{ color: '#f8fafc' }}>3. Collaborate</h3>
            <p style={{ color: '#94a3b8' }}>
              I identify small opportunities to improve stability, always aligned with the team.
            </p>
          </div>
        </SwiperSlide>
      </Swiper>

      <p style={{ textAlign: 'center', fontSize: '0.8rem', color: '#64748b' }}>
        (Swipe cards to navigate)
      </p>
    </div>
  );
}
