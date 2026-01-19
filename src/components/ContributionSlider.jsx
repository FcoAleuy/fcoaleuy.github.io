import React from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import { EffectCards, Pagination } from 'swiper/modules';

import 'swiper/css';
import 'swiper/css/effect-cards';
import 'swiper/css/pagination';

export default function ContributionSlider() {
  const cardStyle = {
    borderRadius: '16px',
    padding: '2rem',
    height: '320px',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    boxSizing: 'border-box',
    boxShadow: '0 10px 30px -10px rgba(0,0,0,0.5)',
    cursor: 'grab',
  };

  return (
    <div style={{ maxWidth: '320px', margin: '0 auto' }}>
      <style>{`
        .swiper {
          width: 100%;
          padding-top: 20px;
          padding-bottom: 40px;
          overflow: visible;
        }
        .swiper-slide {
          border-radius: 16px;
        }
        .swiper-pagination-bullet {
          background: #64748b;
          opacity: 0.5;
        }
        .swiper-pagination-bullet-active {
          background: #38bdf8;
          opacity: 1;
        }
      `}</style>

      <Swiper
        effect="cards"
        grabCursor={true}
        modules={[EffectCards, Pagination]}
        pagination={{ clickable: true }}
      >
        <SwiperSlide>
          <div style={{
            ...cardStyle,
            border: '1px solid #38bdf8',
            background: 'linear-gradient(145deg, #0f172a 0%, #1e293b 100%)',
          }}>
            <h3 style={{ fontSize: '1.2rem', color: '#38bdf8', marginBottom: '1rem' }}>
              1. Understand Context
            </h3>
            <p style={{ color: '#cbd5e1', fontSize: '1rem', lineHeight: '1.6' }}>
              I listen first. I ensure I understand the context, team dynamics, and operational standards before acting.
            </p>
          </div>
        </SwiperSlide>

        <SwiperSlide>
          <div style={{
            ...cardStyle,
            border: '1px solid rgba(56, 189, 248, 0.4)',
            background: 'linear-gradient(145deg, #0f172a 0%, #1e293b 100%)',
          }}>
            <h3 style={{ fontSize: '1.2rem', color: '#f8fafc', marginBottom: '1rem' }}>
              2. Execute Reliably
            </h3>
            <p style={{ color: '#94a3b8', fontSize: '1rem', lineHeight: '1.6' }}>
              I carry out tasks with precision and consistency, reducing errors and workload for the team.
            </p>
          </div>
        </SwiperSlide>

        <SwiperSlide>
          <div style={{
            ...cardStyle,
            border: '1px solid rgba(56, 189, 248, 0.4)',
            background: 'linear-gradient(145deg, #0f172a 0%, #1e293b 100%)',
          }}>
            <h3 style={{ fontSize: '1.2rem', color: '#f8fafc', marginBottom: '1rem' }}>
              3. Collaborate
            </h3>
            <p style={{ color: '#94a3b8', fontSize: '1rem', lineHeight: '1.6' }}>
              I identify small opportunities to improve stability, always aligned with the team.
            </p>
          </div>
        </SwiperSlide>
      </Swiper>

      <p style={{ textAlign: 'center', fontSize: '0.8rem', color: '#64748b', marginTop: '-10px' }}>
        (Swipe cards to navigate)
      </p>
    </div>
  );
}
