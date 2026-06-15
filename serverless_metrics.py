import time
import random

# Simulate serverless function execution
def simulate_inference(request_id):
    """Simulates a serverless inference function and returns metrics."""
    start_time = time.time()
    
    # Simulate model inference time (variable)
    inference_duration = random.uniform(0.1, 1.5) # seconds
    time.sleep(inference_duration)
    
    # Simulate potential errors
    error_occurred = random.random() < 0.05 # 5% chance of error
    
    end_time = time.time()
    duration = end_time - start_time
    
    return {
        "request_id": request_id,
        "inference_duration": inference_duration,
        "total_duration": duration,
        "success": not error_occurred,
        "error_message": "Simulated inference error" if error_occurred else None
    }

# --- Main simulation loop ---
if __name__ == "__main__":
    num_requests = 20
    results = []
    
    print(f"Simulating {num_requests} serverless inference requests...")
    
    for i in range(num_requests):
        request_data = simulate_inference(f"req_{i+1}")
        results.append(request_data)
        print(f"  Request {request_data['request_id']} completed in {request_data['total_duration']:.2f}s (Inference: {request_data['inference_duration']:.2f}s, Success: {request_data['success']})")

    # --- Metric Calculation ---
    total_requests = len(results)
    successful_requests = sum(1 for r in results if r['success'])
    failed_requests = total_requests - successful_requests
    
    # Average total duration (measures end-to-end latency)
    avg_total_duration = sum(r['total_duration'] for r in results) / total_requests if total_requests else 0
    
    # Average inference duration (measures model processing time)
    avg_inference_duration = sum(r['inference_duration'] for r in results if r['success']) / successful_requests if successful_requests else 0
    
    # Error rate
    error_rate = (failed_requests / total_requests) * 100 if total_requests else 0
    
    # P95 total duration (measures tail latency)
    sorted_durations = sorted([r['total_duration'] for r in results])
    p95_index = int(0.95 * total_requests)
    p95_total_duration = sorted_durations[p95_index] if total_requests > 0 else 0

    print("\n--- Performance Metrics ---")
    print(f"Total Requests: {total_requests}")
    print(f"Successful Requests: {successful_requests}")
    print(f"Failed Requests: {failed_requests}")
    print(f"Error Rate: {error_rate:.2f}%")
    print(f"Average Total Duration: {avg_total_duration:.2f}s")
    print(f"Average Inference Duration: {avg_inference_duration:.2f}s")
    print(f"P95 Total Duration: {p95_total_duration:.2f}s")
