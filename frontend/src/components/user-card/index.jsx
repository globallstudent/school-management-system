import React from 'react'

const colors = {
         lamaSky:"#c3ebfa",
         lamaSkyLight:"#edf9fd",
         lamaPurple:"#cfceff",
         lamaPurpleLight:"#f1f0ff",
         lamaYellow:"#fae27c",
         lamaYellowLight:"#fefceb"
}

const UserCard = ({type}) => {
  return (
    <div className={`rounded-2xl odd:bg-[#cfceff] even:bg-[#fae27c] p-4 flex-1 min-w-[130px]`}>
      <div className='flex justify-between items-center'>
        <span className='text-[10px] bg-white px-2 py-1 rounded-full text-green-600'>2024/25</span>
        <img src="/more.png" className='w-[20px] h-[20px]' alt="more" />
      </div>
      <h1 className='text-2xl font-semibold my-4'>1,234</h1>
      <h2 className='capitalize text-sm font-medium text-gray-500'>{type}</h2>
    </div>
  );
}

export default UserCard