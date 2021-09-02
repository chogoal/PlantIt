let date = new Date();
const renderCalender = () => {
  const viewYear = date.getFullYear(); // 년도
  const viewMonth = date.getMonth(); // 월 (0~11 으로 표현)

  document.querySelector('.year-month').textContent = `${viewYear}년 ${viewMonth + 1}월`;

  const prevLast = new Date(viewYear, viewMonth, 0); // 저번 달 마지막 날
  const thisLast = new Date(viewYear, viewMonth + 1, 0); // 이번 달 마지막 날

  const PLDate = prevLast.getDate(); // prevLast의 일자 정보 (0~31)
  const PLDay = prevLast.getDay(); // prevLast의 요일 정보 (0~6/일~토)

  const TLDate = thisLast.getDate(); // thisLast의 일자 정보 (0~31)
  const TLDay = thisLast.getDay(); // thisLast의 요일 정보 (0~6/일~토)

  const prevDates = [];
  const thisDates = [...Array(TLDate + 1).keys()].slice(1); // day list
  const nextDates = [];

  if (PLDay !== 6) { // 만약 저번 달 마지막 요일이 토요일이 아니라면
    for (let i = 0; i < PLDay + 1; i++) {
      prevDates.unshift(PLDate - i);
    } // 저번 달의 일자에서 i 만큼 뺀 값을 더한다 (달력에서 지난 달들 보여주는 거)
  }

  for (let i = 1; i < 7 - TLDay; i++) { // 이번 달 마지막 요일까지
    nextDates.push(i);
  } // 다음 달 넣기 (달력에서 다음 달 보여주는 거)

  const dates = prevDates.concat(thisDates, nextDates); // 날 합치기
  const firstDateIndex = dates.indexOf(1); // 첫째날의 인덱스 찾기
  const lastDateIndex = dates.lastIndexOf(TLDate); // 마지막날의 인덱스 찾기

  dates.forEach((date, i) => {
    const condition = i >= firstDateIndex && i < lastDateIndex + 1
                      ? 'this'
                      : 'other';
    dates[i] = `<div class="date"><span class=${condition}>${date}</span></div>`;
  });

  document.querySelector('.dates').innerHTML = dates.join('');

  const today = new Date();
  if (viewMonth === today.getMonth() && viewYear === today.getFullYear()) {
    for (let date of document.querySelectorAll('.this')) {
      if (+date.innerText === today.getDate()) {
        date.classList.add('today');
        break;
      }
    }
  }
};

renderCalender();

const prevMonth = () => {
  date.setMonth(date.getMonth() - 1);
  renderCalender();
};

const nextMonth = () => {
  date.setMonth(date.getMonth() + 1);
  renderCalender();
};

const goToday = () => {
  date = new Date();
  renderCalender();
};