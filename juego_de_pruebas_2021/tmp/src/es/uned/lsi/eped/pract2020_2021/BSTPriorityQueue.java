package es.uned.lsi.eped.pract2020_2021;

import es.uned.lsi.eped.DataStructures.*;

/*Representa una cola con prioridad implementada mediante un árbol binario de búsqueda de SamePriorityQueue*/
public class BSTPriorityQueue<E> extends Collection<E> implements PriorityQueueIF<E> {

	// LA DEFINICIÓN DE LOS ATRIBUTOS DE LA CLASE ES TAREA DE CADA ESTUDIANTE
	private BSTree<SamePriorityQueue<E>> tree;
	
	/*
	 * Clase privada que implementa un iterador para la * cola con prioridad basada
	 * en secuencia.
	 */
	public class PriorityQueueIterator implements IteratorIF<E> {

		// LA DEFINICIÓN DE LOS ATRIBUTOS DE LA CLASE ES TAREA DE CADA ESTUDIANTE
		private IteratorIF<SamePriorityQueue<E>> treeIterator;
		private IteratorIF<E> subIterator;
		
		/* Constructor por defecto */
		protected PriorityQueueIterator() {
			this.treeIterator = tree.iterator(BSTreeIF.IteratorModes.DIRECTORDER);
			// this.subIterator = this.treeIterator.getNext().iterator();
		}

		/* Devuelve el siguiente elemento de la iteración */
		public E getNext() {
			if (this.subIterator == null || !this.subIterator.hasNext()) {
				// El subiterador se ha quedado sin elementos que recorrer
				// O no se ha llegado a iniciar
				this.subIterator = this.treeIterator.getNext().iterator();
			}
			return this.subIterator.getNext();
		}

		/* Comprueba si queda algún elemento por iterar */
		public boolean hasNext() {
			if (this.subIterator == null) return this.treeIterator.hasNext();
			return this.treeIterator.hasNext() || this.subIterator.hasNext();
		}

		/* Reinicia el iterador a la posición inicial */
		public void reset() {
			this.treeIterator = tree.iterator(BSTreeIF.IteratorModes.DIRECTORDER);
			this.subIterator = null;
		}

	}

	/* OPERACIONES PROPIAS DE ESTA CLASE */

	/*
	 * constructor por defecto: crea cola con prioridad vacía
	 */
	BSTPriorityQueue() {
		this.tree = new BSTree<SamePriorityQueue<E>>(BSTreeIF.Order.ASCENDING);
	}

	/* OPERACIONES PROPIAS DE LA INTERFAZ PRIORITYQUEUEIF */

	/*
	 * Devuelve el elemento más prioritario de la cola y que llegó en primer lugar
	 * 
	 * @Pre !isEmpty()
	 */
	public E getFirst() {
		return this.iterator().getNext();
	}

	/*
	 * Añade un elemento a la cola de acuerdo a su prioridad y su orden de llegada
	 */
	public void enqueue(E elem, int prior) {
		int pos = 1;
		IteratorIF<SamePriorityQueue<E>> iter = this.tree.iterator(BSTreeIF.IteratorModes.DIRECTORDER);
		if (iter.hasNext()){
			// La cola puede tener una SamePriorityQueue en la que insertar elem
			SamePriorityQueue<E> q;
			boolean done = false;
			while (iter.hasNext()) {
				q = iter.getNext();
				if (q.getPriority() == prior) {
					q.enqueue(elem);
					this.size++;
					done = true;
					break;
				}
				else if (q.getPriority() < prior) {
					q = new SamePriorityQueue<E>(prior);
					q.enqueue(elem);
					this.tree.add(q);
					this.size++;
					done = true;
					break;
				}
				pos++;
			}
			if (!done) {
				q = new SamePriorityQueue<E>(prior);
				q.enqueue(elem);
				this.tree.add(q);
				this.size++;
			}
		} else {
			// La cola está vacía
			SamePriorityQueue<E> q = new SamePriorityQueue<E>(prior);
			q.enqueue(elem);
			this.tree.add(q);
			this.size++;
		}
	}

	/*
	 * Elimina el elemento más prioritario y que llegó a la cola en primer lugar
	 * 
	 * @Pre !isEmpty()
	 */
	public void dequeue() {
		IteratorIF<SamePriorityQueue<E>> iterator = this.tree.iterator(BSTreeIF.IteratorModes.DIRECTORDER);
		if (iterator.hasNext()) {
			SamePriorityQueue<E> q = iterator.getNext();
			System.out.println("prior: " + q.getPriority() + " " + this.size + " " + q.size());
			q.dequeue();
			if (q.isEmpty()) {
				this.tree.remove(q);
			}
			this.size--;
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
		return this.tree.isEmpty();
	}

	/* Decide si la cola contiene el elemento dado por parámetro */
	public boolean contains(E e) {
		IteratorIF<E> iterator = this.iterator();
		E comp = iterator.getNext();
		while (iterator.hasNext()) {
			if (comp == e) return true;
		}
		return false;
	}

	/* Elimina todos los elementos de la cola */
	public void clear() {
		this.tree.clear();
	}

}
