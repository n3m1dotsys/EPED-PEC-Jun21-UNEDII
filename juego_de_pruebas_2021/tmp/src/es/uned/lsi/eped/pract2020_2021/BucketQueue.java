package es.uned.lsi.eped.pract2020_2021;

import es.uned.lsi.eped.DataStructures.*;

/*Representa una cola con prioridad implementada mediante una secuencia de SamePriorityQueue*/
public class BucketQueue<E> extends Collection<E> implements PriorityQueueIF<E> {

	// LA DEFINICIÓN DE LOS ATRIBUTOS DE LA CLASE ES TAREA DE CADA ESTUDIANTE
	
	private List<SamePriorityQueue<E>> list;
	
	/*
	 * Clase privada que implementa un iterador para la * cola con prioridad basada
	 * en secuencia.
	 */
	protected class PriorityQueueIterator implements IteratorIF<E> {

		// LA DEFINICIÓN DE LOS ATRIBUTOS DE LA CLASE ES TAREA DE CADA ESTUDIANTE
		
		private IteratorIF<SamePriorityQueue<E>> listIterator;
		private	IteratorIF<E> subIterator; 
		
		/* Constructor por defecto */
		protected PriorityQueueIterator() {
			this.listIterator = list.iterator();
		}
	
		/* Devuelve el siguiente elemento de la iteración */
		public E getNext() {
			if (this.subIterator == null || !this.subIterator.hasNext()){
				// Se ha acabado la cola y hay que pasar a la siguiente
				// O no se ha llegado a iniciar el subiterador
				this.subIterator = this.listIterator.getNext().iterator();
			}
			return this.subIterator.getNext();
		}

		/* Comprueba si queda algún elemento por iterar */
		public boolean hasNext() {
			if (this.subIterator == null) return this.listIterator.hasNext();
			return this.listIterator.hasNext() || this.subIterator.hasNext();
		}

		/* Reinicia el iterador a la posición inicial */
		public void reset() {
			this.listIterator = list.iterator();
			this.subIterator = null;
		}
		
	}

	/* OPERACIONES PROPIAS DE ESTA CLASE */

	/*
	 * constructor por defecto: crea cola con prioridad vacía
	 */
	BucketQueue(){
		this.list = new List<SamePriorityQueue<E>>();
		this.size = 0;
	}

	/* OPERACIONES PROPIAS DE LA INTERFAZ PRIORITYQUEUEIF */

	/*
	 * Devuelve el elemento más prioritario de la cola y que llegó en primer lugar
	 * 
	 * @Pre !isEmpty()
	 */
	public E getFirst() { 
		return this.list.get(1).getFirst();
	}

	/*
	 * Añade un elemento a la cola de acuerdo a su prioridad y su orden de llegada
	 */
	public void enqueue(E elem, int prior) {
		int pos = 1;
		IteratorIF<SamePriorityQueue<E>> iter = this.list.iterator();
		if (iter.hasNext()){
			// La cola puede tener una SamePriorityQueue en la que insertar elem
			SamePriorityQueue<E> q;
			boolean done = false;
			while (iter.hasNext()) {
				q = iter.getNext();
				if (q.getPriority() == prior) {
					q.enqueue(elem);
					this.size++;
					// System.out.println("Encolando elemento con prioridad " + prior + " en posición " + pos + " " + this.size); // TODO DEBUG
					done = true;
					break;
				}
				else if (q.getPriority() < prior) {
					q = new SamePriorityQueue<E>(prior);
					q.enqueue(elem);
					this.list.insert(pos, q);
					this.size++;
					// System.out.println("Encolando elemento con prioridad " + prior + " en posición " + pos + " con una nueva cola " + this.size); // TODO DEBUG
					done = true;
					break;
				}
				pos++;
			}
			if (!done) {
				q = new SamePriorityQueue<E>(prior);
				q.enqueue(elem);
				this.list.insert(pos, q);
				this.size++;
				// System.out.println("Encolando elemento con prioridad " + prior + " en posición " + this.list.size() + " con una nueva cola al final " + this.size); // TODO DEBUG
			}
		} else {
			// La cola está vacía
			SamePriorityQueue<E> q = new SamePriorityQueue<E>(prior);
			q.enqueue(elem);
			this.list.insert(pos, q);
			this.size++;
			// System.out.println("Iniciando la cola con el primer elemento de prioridad " + prior + " " + this.size); // TODO DEBUG 
		}
	}

	/*
	 * Elimina el elemento más prioritario y que llegó a la cola en primer lugar
	 * 
	 * @Pre !isEmpty()
	 */
	public void dequeue() { 
		if (this.size > 0) {
			this.list.get(1).dequeue();
			this.size--;
			// System.out.println("Desencolando " + this.size); // TODO DEBUG
			if (this.list.get(1).isEmpty()) {
				this.list.remove(1);
			}
		}
	}

	/* OPERACIONES PROPIAS DE LA INTERFAZ SEQUENCEIF */

	/* Devuelve un iterador para la cola */
	public IteratorIF<E> iterator() {
		return new PriorityQueueIterator();
	}

	/* OPERACIONES PROPIAS DE LA INTERFAZ COLLECTIONIF */

	/* Devuelve el número de elementos de la cola */
	public int size() {
		return this.size;
	}

	/* Decide si la cola está vacía */
	public boolean isEmpty() { 
		IteratorIF<SamePriorityQueue<E>> iter = this.list.iterator();
		while(iter.hasNext()) {
			if (!iter.getNext().isEmpty()) return false;
		} 
		return true;
	}

	/* Decide si la cola contiene el elemento dado por parámetro */
	public boolean contains(E e) { 
		IteratorIF<E> it = this.iterator();
		while (it.hasNext()) {
			if (it.getNext().equals(e)) return true;
		}
		return false;
	}

	/* Elimina todos los elementos de la cola */
	public void clear() { 
		this.list.clear();
	}

}
