import{m,f as T,s as $,a as H,h as W,b as G,c as N,g as X,j as h,S as R,P as U,d as Y}from"./create-shadow.C8wcRePP.js";import"./index.BmW6Ki2V.js";/* empty css                       */const O='<svg class="swiper-navigation-icon" width="11" height="20" viewBox="0 0 11 20" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M0.38296 20.0762C0.111788 19.805 0.111788 19.3654 0.38296 19.0942L9.19758 10.2796L0.38296 1.46497C0.111788 1.19379 0.111788 0.754138 0.38296 0.482966C0.654131 0.211794 1.09379 0.211794 1.36496 0.482966L10.4341 9.55214C10.8359 9.9539 10.8359 10.6053 10.4341 11.007L1.36496 20.0762C1.09379 20.3474 0.654131 20.3474 0.38296 20.0762Z" fill="currentColor"/></svg>';function F({swiper:t,extendParams:u,on:g,emit:E}){u({navigation:{nextEl:null,prevEl:null,addIcons:!0,hideOnClick:!1,disabledClass:"swiper-button-disabled",hiddenClass:"swiper-button-hidden",lockClass:"swiper-button-lock",navigationDisabledClass:"swiper-navigation-disabled"}}),t.navigation={nextEl:null,prevEl:null,arrowSvg:O};function L(e){let a;return e&&typeof e=="string"&&t.isElement&&(a=t.el.querySelector(e)||t.hostEl.querySelector(e),a)?a:(e&&(typeof e=="string"&&(a=[...document.querySelectorAll(e)]),t.params.uniqueNavElements&&typeof e=="string"&&a&&a.length>1&&t.el.querySelectorAll(e).length===1?a=t.el.querySelector(e):a&&a.length===1&&(a=a[0])),e&&!a?e:a)}function p(e,a){const n=t.params.navigation;e=m(e),e.forEach(i=>{i&&(i.classList[a?"add":"remove"](...n.disabledClass.split(" ")),i.tagName==="BUTTON"&&(i.disabled=a),t.params.watchOverflow&&t.enabled&&i.classList[t.isLocked?"add":"remove"](n.lockClass))})}function v(){const{nextEl:e,prevEl:a}=t.navigation;if(t.params.loop){p(a,!1),p(e,!1);return}p(a,t.isBeginning&&!t.params.rewind),p(e,t.isEnd&&!t.params.rewind)}function f(e){e.preventDefault(),!(t.isBeginning&&!t.params.loop&&!t.params.rewind)&&(t.slidePrev(),E("navigationPrev"))}function x(e){e.preventDefault(),!(t.isEnd&&!t.params.loop&&!t.params.rewind)&&(t.slideNext(),E("navigationNext"))}function o(){const e=t.params.navigation;if(t.params.navigation=T(t,t.originalParams.navigation,t.params.navigation,{nextEl:"swiper-button-next",prevEl:"swiper-button-prev"}),!(e.nextEl||e.prevEl))return;let a=L(e.nextEl),n=L(e.prevEl);Object.assign(t.navigation,{nextEl:a,prevEl:n}),a=m(a),n=m(n);const i=(s,r)=>{if(s){if(e.addIcons&&s.matches(".swiper-button-next,.swiper-button-prev")&&!s.querySelector("svg")){const d=document.createElement("div");$(d,O),s.appendChild(d.querySelector("svg")),d.remove()}s.addEventListener("click",r==="next"?x:f)}!t.enabled&&s&&s.classList.add(...e.lockClass.split(" "))};a.forEach(s=>i(s,"next")),n.forEach(s=>i(s,"prev"))}function l(){let{nextEl:e,prevEl:a}=t.navigation;e=m(e),a=m(a);const n=(i,s)=>{i.removeEventListener("click",s==="next"?x:f),i.classList.remove(...t.params.navigation.disabledClass.split(" "))};e.forEach(i=>n(i,"next")),a.forEach(i=>n(i,"prev"))}g("init",()=>{t.params.navigation.enabled===!1?w():(o(),v())}),g("toEdge fromEdge lock unlock",()=>{v()}),g("destroy",()=>{l()}),g("enable disable",()=>{let{nextEl:e,prevEl:a}=t.navigation;if(e=m(e),a=m(a),t.enabled){v();return}[...e,...a].filter(n=>!!n).forEach(n=>n.classList.add(t.params.navigation.lockClass))}),g("click",(e,a)=>{let{nextEl:n,prevEl:i}=t.navigation;n=m(n),i=m(i);const s=a.target;let r=i.includes(s)||n.includes(s);if(t.isElement&&!r){const d=a.path||a.composedPath&&a.composedPath();d&&(r=d.find(b=>n.includes(b)||i.includes(b)))}if(t.params.navigation.hideOnClick&&!r){if(t.pagination&&t.params.pagination&&t.params.pagination.clickable&&(t.pagination.el===s||t.pagination.el.contains(s)))return;let d;n.length?d=n[0].classList.contains(t.params.navigation.hiddenClass):i.length&&(d=i[0].classList.contains(t.params.navigation.hiddenClass)),E(d===!0?"navigationShow":"navigationHide"),[...n,...i].filter(b=>!!b).forEach(b=>b.classList.toggle(t.params.navigation.hiddenClass))}});const S=()=>{t.el.classList.remove(...t.params.navigation.navigationDisabledClass.split(" ")),o(),v()},w=()=>{t.el.classList.add(...t.params.navigation.navigationDisabledClass.split(" ")),l()};Object.assign(t.navigation,{enable:S,disable:w,update:v,init:o,destroy:l})}function Z({swiper:t,extendParams:u,on:g}){u({coverflowEffect:{rotate:50,stretch:0,depth:100,scale:1,modifier:1,slideShadows:!0}}),H({effect:"coverflow",swiper:t,on:g,setTranslate:()=>{const{width:p,height:v,slides:f,slidesSizesGrid:x}=t,o=t.params.coverflowEffect,l=t.isHorizontal(),S=t.translate,w=l?-S+p/2:-S+v/2,e=l?o.rotate:-o.rotate,a=o.depth,n=W(t);for(let i=0,s=f.length;i<s;i+=1){const r=f[i],d=x[i],b=r.swiperSlideOffset,B=(w-b-d/2)/d,c=typeof o.modifier=="function"?o.modifier(B):B*o.modifier;let j=l?e*c:0,M=l?0:e*c,P=-a*Math.abs(c),y=o.stretch;typeof y=="string"&&y.indexOf("%")!==-1&&(y=parseFloat(o.stretch)/100*d);let I=l?0:y*c,q=l?y*c:0,z=1-(1-o.scale)*Math.abs(c);Math.abs(q)<.001&&(q=0),Math.abs(I)<.001&&(I=0),Math.abs(P)<.001&&(P=0),Math.abs(j)<.001&&(j=0),Math.abs(M)<.001&&(M=0),Math.abs(z)<.001&&(z=0);const A=`translate3d(${q}px,${I}px,${P}px)  rotateX(${n(M)}deg) rotateY(${n(j)}deg) scale(${z})`,D=G(o,r);if(D.style.transform=A,r.style.zIndex=-Math.abs(Math.round(c))+1,o.slideShadows){let C=l?r.querySelector(".swiper-slide-shadow-left"):r.querySelector(".swiper-slide-shadow-top"),k=l?r.querySelector(".swiper-slide-shadow-right"):r.querySelector(".swiper-slide-shadow-bottom");C||(C=N("coverflow",r,l?"left":"top")),k||(k=N("coverflow",r,l?"right":"bottom")),C&&(C.style.opacity=c>0?c:0),k&&(k.style.opacity=-c>0?-c:0)}}},setTransition:p=>{t.slides.map(f=>X(f)).forEach(f=>{f.style.transitionDuration=`${p}ms`,f.querySelectorAll(".swiper-slide-shadow-top, .swiper-slide-shadow-right, .swiper-slide-shadow-bottom, .swiper-slide-shadow-left").forEach(x=>{x.style.transitionDuration=`${p}ms`})})},perspective:()=>!0,overwriteParams:()=>({watchSlidesProgress:!0})})}function K(){const t=[{img:"/assets/aws.jpg",title:"AWS Strategy",desc:"Infrastructure evaluation and strategic cloud alignment."},{img:"/assets/IBM.jpg",title:"IBM AI Discovery",desc:"Exploring Watson capabilities for enterprise automation."},{img:"/assets/Google.JPEG",title:"Innovation Culture",desc:"Understanding the operational scale and culture of global technology leaders."},{img:"/assets/Amelia.jpeg",title:"Global Benchmarking",desc:"Evaluating conversational AI solutions at EXPORC Madrid."},{img:"/assets/gocontact.png",title:"CCaaS Evaluation",desc:"Assessing cloud contact center platforms to modernize support operations."},{img:"/assets/smartcontact.png",title:"Process Automation",desc:"Implementing NLU and multichannel bots to reduce operational friction."},{img:"/assets/kanban.png",title:"Product Discovery",desc:"Leading discovery, process mapping, and feature prioritization."},{img:"/assets/Credenciales.png",title:"Enterprise Standards",desc:"Operating within strict frameworks for compliance and security."}];return h.jsxs("div",{style:{width:"100%",maxWidth:"1200px",margin:"0 auto",padding:"2rem 0",overflow:"hidden"},children:[h.jsx("style",{children:`
        .enterprise-swiper {
          padding-bottom: 50px !important;
          padding-top: 20px !important;
        }
        
        .enterprise-swiper .swiper-slide {
          width: 300px; 
          height: auto;
          transition: all 0.3s ease;
          opacity: 0.4;
          transform: scale(0.9);
        }

        @media (min-width: 768px) {
          .enterprise-swiper .swiper-slide {
            width: 380px; 
          }
        }

        .enterprise-swiper .swiper-slide-active {
          opacity: 1;
          transform: scale(1);
          z-index: 10;
          box-shadow: 0 0 40px rgba(56, 189, 248, 0.15);
        }

        .slide-card {
          position: relative;
          border-radius: 16px;
          overflow: hidden;
          background: #0f172a;
          border: 1px solid rgba(56, 189, 248, 0.2);
          height: 100%;
          display: flex;
          flex-direction: column;
        }

        .slide-card img {
          width: 100%;
          height: 320px; 
          object-fit: cover;
          object-position: center top; 
          display: block;
        }

        @media (min-width: 768px) {
          .slide-card img {
            height: 400px; 
          }
        }
        
        .slide-caption {
          padding: 1.5rem;
          background: #0f172a;
          text-align: left;
          border-top: 1px solid rgba(56, 189, 248, 0.1);
          flex-grow: 1;
        }

        .swiper-button-next, .swiper-button-prev {
          color: #38bdf8;
          background: rgba(15, 23, 42, 0.85);
          width: 44px;
          height: 44px;
          border-radius: 50%;
          border: 1px solid rgba(56, 189, 248, 0.4);
          backdrop-filter: blur(4px);
        }
        .swiper-button-next:after, .swiper-button-prev:after {
          font-size: 1.2rem;
          font-weight: bold;
        }
        
        .swiper-pagination-bullet { background: #64748b; }
        .swiper-pagination-bullet-active { background: #38bdf8; }
      `}),h.jsx(R,{modules:[F,U,Z],effect:"coverflow",grabCursor:!0,centeredSlides:!0,slidesPerView:"auto",coverflowEffect:{rotate:0,stretch:0,depth:100,modifier:2.5,slideShadows:!1},loop:!0,navigation:!0,pagination:{clickable:!0},className:"enterprise-swiper",children:t.map((u,g)=>h.jsx(Y,{children:h.jsxs("div",{className:"slide-card",children:[h.jsx("img",{src:u.img,alt:u.title,loading:"lazy"}),h.jsxs("div",{className:"slide-caption",children:[h.jsx("div",{style:{color:"#38bdf8",fontWeight:"700",marginBottom:"0.4rem",fontSize:"1.1rem"},children:u.title}),h.jsx("div",{style:{color:"#94a3b8",fontSize:"0.95rem",lineHeight:"1.5"},children:u.desc})]})]})},g))})]})}export{K as default};
