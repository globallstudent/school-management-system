import { create } from "zustand";


const useLayoutStore = create((set) => ({
  isOpen: false,
  setIsOpen: (value) => set({isOpen:value})
}))

export default useLayoutStore;