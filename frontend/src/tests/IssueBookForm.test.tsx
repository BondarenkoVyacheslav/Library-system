// frontend/src/tests/IssueBookForm.test.tsx
test('displays success message after issuing book', async () => {
    jest.spyOn(api, 'issueBook').mockResolvedValueOnce({ success: true })
    render(<IssueBookForm bookId={1} />)
    
    fireEvent.change(screen.getByPlaceholderText('ID читателя'), { 
      target: { value: '123' } 
    })
    fireEvent.click(screen.getByText('Выдать книгу'))
    
    await waitFor(() => {
      expect(screen.getByText('Книга успешно выдана')).toBeInTheDocument()
    })
  })