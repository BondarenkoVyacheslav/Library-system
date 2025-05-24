// frontend/src/components/IssueBookForm.tsx
import { useState } from 'react'
import { useAppSelector } from '../store/hooks'
import { issueBook } from '../api/books'

export default function IssueBookForm({ bookId }: { bookId: number }) {
  const [readerId, setReaderId] = useState('')
  const { token } = useAppSelector(state => state.auth)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
      await issueBook(token, bookId, parseInt(readerId))
      alert('Книга успешно выдана')
    } catch (err) {
      alert('Ошибка при выдаче книги')
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="number" 
        value={readerId}
        onChange={(e) => setReaderId(e.target.value)}
        placeholder="ID читателя"
      />
      <button type="submit">Выдать книгу</button>
    </form>
  )
}