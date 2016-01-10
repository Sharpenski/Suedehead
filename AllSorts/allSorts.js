function quickSort(array, lo, hi) {
	if(lo < hi) {
		var pivot = partition(array, lo, hi);
		quickSort(array, lo, pivot-1);
		quickSort(array, pivot+1, hi);
	}
	return array;
}

function partition(array, lo, hi) {
	var pivot = array[hi];
	i = lo;
	for(var j = lo; j < hi; j++) {
		if(array[j] <= pivot) {
			swap(array,i,j);
			i++; // move the wall up 1 place
		}
	}
	swap(array,i,hi);
	return i;
}

function bubbleSort(array) {
	var swapped = true;
	while (swapped == true) {
		swapped = false;
		for(var i = 1; i < array.length; i++) {
			if (array[i-1] > array[i]) {
				swap(array, i-1, i);
				swapped = true;
			}
		}
	}
	console.log("Bubble sorted:", array);
	return array;
}

function selectionSort(array) {
	for(var i = 0; i < array.length; i++) {
		var minimum = i;
		for(var j = i+1; j < array.length; j++) {
			if(array[j] < array[minimum]) {
				minimum = j;
			}
		}
		swap(array,i,minimum);
	}
	console.log("Selection sorted:", array);
	return array;
}

function insertionSort(array) {
	for(var i = 1; i < array.length; i++) {
		var j = i;
		while(array[j-1] > array[j] && j > 0) {
			swap(array,j-1,j);
			j--;
		}
	}
	console.log("Insertion sorted:", array);
	return array;
}

function mergeSort(array, lo, hi, workArray) {
	if(array.length < 2) {
		return array;
	} else {
		var mid = Math.floor((hi+lo) / 2);
		mergeSort(array, lo, mid, workArray);
		mergeSort(array, mid+1, hi, workArray);
		merge(array, lo, mid, hi, workArray);
		CopyArray(B, lo, hi, A);
	}

}

function merge(A, lo, mid, hi, B) {
	var i = lo, j = mid;
	for(var k = lo; k < hi; k++) {
		if(i < mid && (j >= hi || array[i] <= array[j])) {
			B[k] = A[i];
			i++;
		} else {
			B[k] = A[j];
			j++;
		}
	}
}

function CopyArray(workArray, lo, hi, array) {
	for(var k = lo; k < hi; k++) {
		array[k] = workArray[k];
	}
}

function swap(array, i, j) {
	var temp = array[i];
	array[i] = array[j];
	array[j] = temp;
}

var unsorted = [4,3,2,1,6];
document.getElementById("sel").innerHTML = selectionSort(unsorted);